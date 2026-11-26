"""Local-only NAVER Maps proxy. Run with: py gyeotae-maps-local.py"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
APP = ROOT / "gyeotae-s25-ultra.html"
ROUTES = {
    "/api/static-map": "https://maps.apigw.ntruss.com/map-static/v2/raster",
    "/api/directions": "https://maps.apigw.ntruss.com/map-direction/v1/driving",
    "/api/geocode": "https://maps.apigw.ntruss.com/map-geocode/v2/geocode",
}

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def send_body(self, status, payload, content_type="application/json; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def problem(self, status, message):
        self.send_body(status, json.dumps({"error": message}).encode())

    def do_GET(self):
        request = urlsplit(self.path)
        hosts = {"localhost:8765", "127.0.0.1:8765"}
        if self.headers.get("Host") not in hosts:
            return self.problem(403, "로컬 주소에서 실행해 주세요.")
        if request.path in ("/", "/gyeotae-s25-ultra.html"):
            if not APP.is_file():
                return self.problem(404, "서버 파일과 HTML을 같은 폴더에 넣어 주세요.")
            return self.send_body(200, APP.read_bytes(), "text/html; charset=utf-8")
        endpoint = ROUTES.get(request.path)
        if not endpoint:
            return self.problem(404, "지원하지 않는 경로예요.")
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://{host}" for host in hosts}:
            return self.problem(403, "같은 페이지에서 요청해 주세요.")
        if self.headers.get("Sec-Fetch-Site") not in (None, "same-origin"):
            return self.problem(403, "같은 페이지에서 요청해 주세요.")
        key_id = os.environ.get("GYEOTAE_MAPS_KEY_ID") or self.headers.get("x-ncp-apigw-api-key-id")
        key = os.environ.get("GYEOTAE_MAPS_KEY") or self.headers.get("x-ncp-apigw-api-key")
        if not key_id:
            return self.problem(428, "서버에 GYEOTAE_MAPS_KEY_ID를 설정해 주세요.")
        if not key:
            return self.problem(428, "곁에 설정에서 API 키를 입력해 주세요.")
        upstream = Request(f"{endpoint}?{request.query}", headers={
            "Accept": "image/png" if request.path == "/api/static-map" else "application/json",
            "x-ncp-apigw-api-key-id": key_id,
            "x-ncp-apigw-api-key": key,
        })
        try:
            with urlopen(upstream, timeout=12) as result:
                self.send_body(result.status, result.read(), result.headers.get("Content-Type", "application/json"))
        except HTTPError as error:
            self.send_body(error.code, error.read())
        except (URLError, TimeoutError, ValueError):
            self.problem(502, "네이버 지도 서버에 연결하지 못했어요.")

if __name__ == "__main__":
    with ThreadingHTTPServer(("127.0.0.1", 8765), Handler) as server:
        print("곁에 http://localhost:8765", flush=True)
        server.serve_forever()
