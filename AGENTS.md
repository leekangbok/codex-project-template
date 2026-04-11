# AGENTS 안내

이 파일은 에이전트가 이 저장소를 빠르게 이해하기 위한 짧은 지도 역할을 합니다.
모든 세부 지식을 이 파일에 몰아넣지 말고, 아래 문서들로 이동하는 목차로 사용하세요.

## 먼저 읽을 것

1. `README.md`
2. `WORKFLOW.md`
3. `AI_RULES.md`
4. `HARNESS.md`
5. `CONTEXT.md`
6. `TASKS.md`

## 목적별 문서 위치

- 현재 상태와 다음 작업
  `CONTEXT.md`, `TASKS.md`
- 아키텍처와 모듈 경계
  `docs/architecture.md`, `docs/DESIGN.md`, `docs/FRONTEND.md`
- 실행 계획과 기술 부채
  `docs/exec-plans/active/`, `docs/exec-plans/completed/`, `docs/exec-plans/tech-debt-tracker.md`
- 제품 요구사항과 사용자 흐름
  `docs/product-specs/`
- 검증 및 품질 기준
  `HARNESS.md`, `docs/QUALITY.md`, `docs/RELIABILITY.md`, `docs/SECURITY.md`
- AI 에이전트 스킬 및 워크플로우
  `skills/README.md`, `skills/` 디렉토리 전체
- 참고 자료와 외부 레퍼런스
  `docs/references/`
- 자동 생성 자료
  `docs/generated/`

## 에이전트 작업 원칙

- 코드를 수정하기 전에 관련 문서를 먼저 찾습니다.
- 큰 지시 파일 하나에 의존하지 말고, 필요한 문서를 찾아 읽습니다.
- 코드 변경 후에는 `scripts/check.*` 또는 프로젝트별 검증 명령을 우선 실행합니다.
- 테스트 통과 전에는 다음 단계로 진행하지 않습니다.
- 문서와 실제 상태가 어긋나면 관련 문서를 함께 갱신합니다.

## 문서 확장 규칙

- 새로운 도메인 지식은 `docs/` 아래 적절한 위치에 추가합니다.
- 이 파일에는 세부 내용을 길게 적지 말고, 문서 위치만 연결합니다.
- 자주 참조되는 새 문서가 생기면 이 파일의 목차를 갱신합니다.
