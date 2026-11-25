# Jira 작업 계획

기한: **2026-11-26** (내일). 준비 작업은 오늘(2026-11-25)까지입니다.

Jira에는 [`jira-import.csv`](jira-import.csv)를 가져오면 에픽 6개와 작업 34개가 한 번에 만들어집니다. 담당자(Assignee)는 가져온 뒤 지정하세요.

## 가져오는 방법

1. Jira 프로젝트 > 프로젝트 설정 또는 상단 `...` > **Import issues from CSV** (시스템 설정 > 외부 시스템 가져오기 > CSV)
2. `docs/jira-import.csv` 선택, 인코딩 UTF-8
3. 필드 매핑: `Issue Id` -> Issue Id, `Parent` -> Parent, `Issue Type` -> Issue Type, `Summary`, `Priority`, `Original Estimate`, `Due Date`(형식 yyyy-MM-dd), `Labels`, `Description`
4. 에픽이 안 이어지면 `Parent` 대신 `Epic Link`로 매핑 (프로젝트 유형에 따라 다름)

## 우선순위 기준

- **Highest / High**: P0, 시연에 꼭 필요
- **Medium**: P1, 되면 좋은 것 (안 되면 미리 만든 값으로 시연)
- **Low**: P2, 시간 남을 때

## 에픽과 작업

### [준비] 기획 확정과 환경 세팅 (6h)

시작 전에 정해야 할 것 정리 · 기한 2026-11-25

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| AI 서비스 결정 (Gemini 또는 OpenAI)과 API 키 발급 | Task | Highest | 0.5h | 11-25 |
| 시연 목적지 2~3곳 선정 (같은 이름 2곳인 장소 포함)과 경로 정의 | Task | Highest | 1h | 11-25 |
| 안내 문장 목록 확정 (약 25개) | Task | Highest | 1h | 11-25 |
| 목소리 복제 팀원 동의 받고 일레븐랩스로 음성 파일 제작 | Task | Highest | 2h | 11-25 |
| frontend 프로젝트 뼈대와 GitHub Pages(https) 배포 설정 | Task | High | 1h | 11-25 |
| 카카오 택시 앱 링크 준비와 폰에서 열리는지 확인 | Task | High | 0.5h | 11-25 |

### [아바타·목소리] 말하는 가족 아바타 (7h)

브랜치 feature/pet-avatar · 기한 2026-11-26

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| 샘플 아바타 이미지 준비 | Story | Highest | 1h | 11-26 |
| 말하는 아바타 화면 UI (영상통화 느낌, 'AI 도우미' 표시) | Story | Highest | 2h | 11-26 |
| 아바타 입 움직임 (Web Audio 소리 크기 연동) | Story | Highest | 2h | 11-26 |
| 눈 깜빡임과 작은 움직임 | Task | Medium | 1h | 11-26 |
| 음성 파일 재생 모듈 (문장 ID로 재생, 재생 끝 이벤트) | Task | Highest | 1h | 11-26 |

### [음성 대화] 듣고 답하기 (7.5h)

브랜치 feature/chatbot · 기한 2026-11-26

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| 음성 인식 (Web Speech API)과 큰 말하기 버튼 | Story | Highest | 2h | 11-26 |
| 짧은 응답 해석 (응/아니/알겠어/다시/잠깐) | Task | Highest | 1.5h | 11-26 |
| 도우미가 말하는 동안 듣지 않고 끝난 뒤 듣기 | Task | High | 1h | 11-26 |
| 실패 대비 선택 버튼과 '다시 알려줘' 버튼 | Task | Highest | 1h | 11-26 |
| AI 말뜻 이해 (아픈데 병원 가야지 -> 목적지 요청) (P1) | Story | Medium | 2h | 11-26 |

### [길안내·택시] 시연 핵심 흐름 (12.5h)

브랜치 feature/navigation · 기한 2026-11-26

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| 대화 흐름 상태 관리 (목적지 -> 확인 -> 이동수단 -> 안내 -> 도착) | Story | Highest | 2h | 11-26 |
| 같은 이름 장소 확인 (가까운 곳부터 지역과 함께 '맞아요?') | Story | Highest | 1.5h | 11-26 |
| 가상 위치 기반 한 단계씩 길 안내 | Story | Highest | 2.5h | 11-26 |
| 택시 부르기 (타는 곳 확인, 카카오 택시 연결, 기다리기 안내) | Story | Highest | 2.5h | 11-26 |
| 도착 칭찬 ('잘 오셨어요!') | Task | Medium | 0.5h | 11-26 |
| 카메라로 방향 보기 (큰 화살표 겹치기) (P1) | Story | Medium | 2h | 11-26 |
| 지도 보기 목업 (현재 위치, 목적지, 경로) (P1) | Task | Low | 1.5h | 11-26 |

### [가족 설정] 가족이 준비하는 화면 (P1) (7.5h)

브랜치 feature/family-setup. 안 되면 미리 설정한 값으로 시연 · 기한 2026-11-26

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| 가족 설정 화면 뼈대 | Task | Medium | 1h | 11-26 |
| 가족 문장 녹음 (MediaRecorder) | Story | Medium | 1.5h | 11-26 |
| 자주 가는 곳 등록 (이름, 주소) | Task | Medium | 1h | 11-26 |
| 사진 올리기, 동의 확인, 아바타 변환 | Story | Medium | 2.5h | 11-26 |
| 입 위치 맞추기와 미리 듣기 | Task | Low | 1.5h | 11-26 |

### [통합·발표] 통합, 테스트, 발표 준비 (8h)

develop -> main 최종 병합 포함 · 기한 2026-11-26

| 작업 | 유형 | 우선순위 | 예상 | 기한 |
| --- | --- | --- | --- | --- |
| P0 기능 통합 (처음부터 끝까지 시연 흐름 완성) | Story | Highest | 2h | 11-26 |
| 폰 실기 테스트 (https 배포, 마이크, 카메라 권한) | Task | Highest | 1.5h | 11-26 |
| 실패 시나리오 점검 (음성 인식 실패, 링크 실패 대체안) | Task | High | 1h | 11-26 |
| 발표 자료 작성 (미리 만든 목소리, 가상 위치, AI 도우미 표시 명시) | Task | High | 2h | 11-26 |
| 시연 리허설 | Task | High | 1h | 11-26 |
| develop -> main 최종 병합 | Task | High | 0.5h | 11-26 |

## 일정 감각

- 전체 예상 합계 48.5h, P0(Highest/High) 34h. 합계가 팀 가용 시간(인원 x 14h)을 넘으면 Medium 이하부터 줄입니다.
- 순서: **E1 준비(오늘)** -> E4 상태 관리 뼈대 먼저 -> E2·E3·E4 병렬 -> E6 통합 -> P1 -> 리허설
- 브랜치 이름은 에픽 이름과 같게 (`feature/pet-avatar`, `feature/chatbot`, `feature/navigation`, `feature/family-setup`)
- 커밋/PR 메시지에 Jira 키(예: `HK-12`)를 넣으면 추적이 쉽습니다.
