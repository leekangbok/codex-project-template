# 프로젝트 진행 워크플로우

이 문서는 이 템플릿으로 실제 프로젝트를 시작하고 운영하는 가장 실용적인 순서를 설명합니다.

## 한눈에 보는 순서

1. 새 프로젝트 생성
2. 질문형 초기 설정 실행
3. 검증 하네스 채우기
4. 첫 작업 정의
5. 구현
6. 검증 통과
7. 문서 갱신
8. 다음 작업 진행

## 1. 프로젝트 시작

새 프로젝트를 만들고 나면 아래 순서로 진행합니다.

### 1-1. 새 프로젝트 생성

템플릿으로 새 프로젝트를 만듭니다.

### 1-2. 질문형 초기 설정 실행

`scripts/project-intake.*`를 실행해서 프로젝트 기본 정보를 입력합니다.

이 단계에서 자동으로 채워지는 문서:

- `README.md`
- `CONTEXT.md`
- `TASKS.md`
- `docs/architecture.md`
- `HARNESS.md`

### 1-3. 검증 하네스 설정

다음으로 `scripts/check.py`를 프로젝트에 맞게 수정합니다.

기본 스타터 프로필은 Python/FastAPI 기준입니다.
필요하면 다른 스택 예시를 `docs/references/check-examples.md`에서 참고해 바꿉니다.

## 2. 세션 시작 루틴

새 Codex 세션을 시작할 때는 아래 순서를 따릅니다.

1. `AGENTS.md`
2. `README.md`
3. `WORKFLOW.md`
4. `AI_RULES.md`
5. `HARNESS.md`
6. `CONTEXT.md`
7. `TASKS.md`
8. 필요하면 `docs/architecture.md`

## 3. 작업 단위 진행 방법

하나의 작업은 아래 순서로 진행합니다.

1. `TASKS.md`에서 다음 작업 선택
2. 관련 코드와 문서 확인
3. 구현 또는 수정
4. `scripts/check.*` 실행
5. 실패 시 수정 후 재검증
6. 검증 통과 후 관련 문서 갱신
7. `python scripts/auto_codex_context.py` 실행
8. `TASKS.md`, `CONTEXT.md` 정리

## 4. 핵심 규칙

- 코드 변경 후에는 반드시 검증을 수행합니다.
- 테스트 또는 검증이 통과하기 전에는 다음 단계로 넘어가지 않습니다.
- 코드와 문서는 같은 작업 안에서 함께 갱신합니다.
- 검증을 못 했으면 이유를 반드시 남깁니다.

## 5. 완료 조건

다음 조건을 모두 만족해야 작업 완료로 봅니다.

- 코드 변경 완료
- 관련 문서 갱신 완료
- `scripts/check.*` 또는 관련 검증 통과
- 남은 리스크 명시

## 6. AI에게 요청하는 방법

좋은 요청은 아래 요소를 포함합니다.

- 목표
- 제약 조건
- 참고 문서
- 완료 기준

예시:

```text
AGENTS.md, WORKFLOW.md, HARNESS.md, CONTEXT.md, TASKS.md를 먼저 읽고,
로그인 API를 추가해줘.

제약:
- 기존 auth 구조 유지
- 테스트 추가

완료 기준:
- scripts/check.py 통과
- docs/architecture.md 갱신
- CONTEXT.md, TASKS.md 반영
```

## 7. 권장 운영 습관

- 큰 작업은 `docs/exec-plans/active/`에 먼저 계획 문서로 정리합니다.
- 제품 요구사항은 `docs/product-specs/`에 남깁니다.
- 기술 부채는 `docs/exec-plans/tech-debt-tracker.md`에 누적합니다.
- 참고 자료는 `docs/references/`에 정리합니다.

## 8. 일일 운영 루프

하루 작업 흐름 예시:

1. `CONTEXT.md`, `TASKS.md` 확인
2. 오늘 작업 목표 선택
3. Codex로 구현
4. 하네스 실행
5. 실패 수정
6. 통과 후 문서 정리
7. 상태 기록

## 9. 피해야 할 방식

- 테스트 없이 다음 작업으로 넘어가기
- 문서 갱신을 미루기
- 큰 지시를 한 번에 던지고 검증 없이 수용하기
- `scripts/check.py`를 비워둔 채 오래 사용하는 것
