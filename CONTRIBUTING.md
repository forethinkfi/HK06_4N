# 팀 Git 사용 규칙

14시간 프로젝트라 **단순하고 지키기 쉬운 규칙**만 정했습니다.

## 1. 최초 1회 설정

```bash
git clone https://github.com/forethinkfi/HK06_4N.git
cd HK06_4N
git checkout develop
cp .env.example .env     # 본인 API 키 입력 (커밋 금지)
```

## 2. 브랜치 규칙

| 브랜치 | 규칙 |
| --- | --- |
| `main` | 시연/제출용. **직접 푸시 금지**, 마지막에 `develop` → `main` 병합 (팀장 담당) |
| `develop` | 통합 브랜치. **직접 푸시 금지**, PR로만 병합 |
| `feature/*` | 기능 개발. 본인 브랜치에서만 작업 |
| `fix/*` | 버그 수정 |

기본 담당 브랜치
- `feature/pet-avatar`: 펫봇 외형 생성
- `feature/floating-ui`: 화면 위 플로팅 UI
- `feature/chatbot`: AI 챗봇

새 브랜치가 필요하면 항상 `develop`에서 만듭니다.

```bash
git checkout develop
git pull
git checkout -b feature/작업명
```

## 3. 하루 작업 흐름

```bash
# 1) 작업 시작 전: 최신 develop 받아서 내 브랜치에 합치기
git checkout feature/내브랜치
git pull origin develop

# 2) 작업 후: 커밋
git add 변경한파일
git commit -m "feat: 펫봇 이미지 업로드 추가"

# 3) 푸시
git push origin feature/내브랜치
```

그다음 GitHub에서 **`develop` 대상으로 Pull Request** 를 만듭니다.

## 4. 커밋 메시지

형식: `type: 내용`

| type | 의미 |
| --- | --- |
| `feat` | 새 기능 |
| `fix` | 버그 수정 |
| `docs` | 문서 |
| `style` | 디자인/포맷 (동작 변화 없음) |
| `refactor` | 구조 개선 |
| `chore` | 설정, 기타 |

예: `feat: 챗봇 음성 입력 추가`, `fix: 펫봇 드래그 안 되는 문제 수정`

## 5. Pull Request 규칙

- 대상은 항상 **`develop`**
- PR 템플릿의 체크리스트를 채우기
- **최소 1명 확인 후 병합** (급하면 팀 채팅에 알리고 병합)
- 작게, 자주 올리기: 1~2시간마다 PR 권장 (오래 들고 있으면 충돌이 커짐)
- 병합은 PR을 올린 사람이 직접

## 6. 충돌 방지

- 담당 폴더/파일을 나눠서 작업 (다른 사람 파일은 먼저 말하고 수정)
- 공용 파일(`README.md`, 설정 파일, 패키지 파일)은 수정 전에 팀 채팅에 공지
- 충돌이 나면 혼자 고민하지 말고 바로 팀원에게 요청

## 7. 절대 금지

- `main`, `develop`에 직접 푸시
- `git push --force` (강제 푸시)
- API 키, 비밀번호, `.env` 커밋 (실수로 올렸다면 **즉시 키 폐기 후 팀에 알림**)
- 용량 큰 파일(영상 등) 커밋. 필요하면 링크로 공유
- 손주 **실제 사진**을 저장소에 올리기. 테스트는 샘플 이미지로, 실제 사진은 개인정보이므로 공개 저장소에 올리지 않기

## 8. 문제가 생기면

| 상황 | 해결 |
| --- | --- |
| 커밋 전에 변경 취소 | 팀원에게 먼저 물어보기 (되돌리면 작업이 사라짐) |
| 브랜치를 잘못 만듦 | 삭제하지 말고 팀에 공유 |
| 푸시가 거부됨 | `git pull origin 내브랜치` 후 다시 푸시 |
| 잘 모르겠음 | 임의로 `reset`, `force` 쓰지 말고 팀에 질문 |
