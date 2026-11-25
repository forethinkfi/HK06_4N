# HK06_4N

프로젝트 소개를 여기에 작성하세요.

## 브랜치 전략

| 브랜치 | 용도 |
| --- | --- |
| `main` | 배포 가능한 안정 버전 |
| `develop` | 개발 통합 브랜치 (기능 브랜치의 병합 대상) |
| `feature/*` | 기능 개발 (`develop`에서 분기) |
| `fix/*` | 버그 수정 |
| `docs/*` | 문서 작업 |

## 작업 흐름

1. `develop`에서 `feature/<작업명>` 브랜치 생성
2. 작업 후 커밋, 푸시
3. `develop`으로 Pull Request
4. 리뷰 후 병합, 릴리스 시 `develop` → `main`

## 커밋 메시지

`type: 내용` 형식 (`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`)
