# 곁에 Netlify 배포

`public/`에 HTML이 있고, `netlify/functions/`의 함수가 네이버 지도, 도보 경로, Gemini 3.8 Live에 요청합니다. Netlify에서 Python을 실행할 필요가 없습니다. 방문자는 앱에 API 키를 입력하지 않습니다. 지도 표시에 필요한 네이버 Client ID는 브라우저에 전달되고, Client Secret과 음성·도보 키는 서버에서 사용합니다.

## Netlify에 직접 배포

1. Netlify에 프로젝트를 만들고 프로젝트 설정의 **Environment variables**에 아래 이름으로 값을 입력합니다. Production에서 사용할 수 있게 하고, 범위를 선택할 수 있으면 **Functions**를 포함합니다.

   | 환경 변수 | 값 |
   | --- | --- |
   | `GYEOTAE_MAPS_KEY_ID` | 네이버 지도 Client ID |
   | `GYEOTAE_MAPS_KEY` | 네이버 지도 Client Secret |
   | `GEMINI_API_KEY` | Google AI Studio API 키 |
   | `ORS_API_KEY` | openrouteservice 도보 API 키 |

2. Node.js 22 이상이 설치된 PC에서 압축을 풀고 `netlify.toml`이 있는 폴더에서 아래 명령을 실행합니다. Netlify의 로그인 화면에서 로그인합니다. 프로젝트 ID는 Netlify 프로젝트 설정에서 확인합니다. [Netlify CLI 배포 문서](https://docs.netlify.com/api-and-cli-guides/cli-guides/get-started-with-cli/)

   ```powershell
   npx netlify-cli login
   npx netlify-cli deploy --prod --site '프로젝트-ID'
   ```

## GitHub Secrets로 배포

이미 GitHub Secrets에 등록한 값을 사용하려면 압축의 구조를 저장소 루트에 복사합니다. `.github/workflows/deploy-gyeotae-netlify.yml`을 기존 워크플로와 함께 둡니다. GitHub **Settings → Secrets and variables → Actions**에서 표에 있는 네 가지 키를 확인하고, `NETLIFY_AUTH_TOKEN`을 Secret으로, `NETLIFY_SITE_ID`를 Repository variable로 설정합니다. 토큰은 GitHub에 직접 입력합니다.

워크플로 파일이 기본 브랜치에 반영되면 GitHub **Actions → Deploy Gyeotae to Netlify → Run workflow**에서 수동 실행합니다. 이 작업이 실행되면 같은 이름의 Netlify Production 환경 변수를 갱신하고 배포합니다. [GitHub Actions 수동 실행](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow) · [Netlify 함수 환경 변수](https://docs.netlify.com/build/functions/environment-variables/)

## 배포 후 확인

1. 네이버 클라우드 Maps Application의 웹 서비스 URL에 `https://사이트이름.netlify.app`을 등록합니다. **Dynamic Map**, **Static Map**, **Geocoding**, **Directions 5**를 활성화합니다. [네이버 지도 Client ID 가이드](https://navermaps.github.io/maps.js.en/docs/tutorial-1-Getting-Client-ID.html)
2. Netlify 공개 주소에서 **지도 보기 → 길 안내**를 열어 자동차와 도보 경로를 각각 확인합니다. 마이크 권한을 허용하고 음성 안내도 확인합니다.
