# Codex CLI 프로젝트 템플릿

이 저장소는 Codex CLI 기반으로 새 프로젝트를 시작할 때 바로 복제해서 사용할 수 있는 실전용 템플릿입니다.
목적은 프로젝트 규칙, 현재 문맥, 작업 목록, 아키텍처를 분리해 새로운 Codex 세션이 상태를 빠르게 복구하고 안전하게 작업하도록 만드는 것입니다.

## 이 템플릿이 해결하는 문제

- 프로젝트 시작 구조가 매번 달라지는 문제
- AI 세션이 충분한 문맥 없이 시작되는 문제
- 코드 변경이 문서에 반영되지 않는 문제
- 세션이 바뀔 때 설계와 진행 이력이 끊기는 문제

## 포함 구조

- `README.md`
  프로젝트 개요, 작업 흐름, 사용 방법
- `AGENTS.md`
  에이전트를 위한 짧은 지도형 문서
- `AI_RULES.md`
  Codex 및 AI 에이전트가 따라야 하는 필수 운영 규칙
- `CONTEXT.md`
  현재 프로젝트 상태, 리스크, 부족한 정보, 다음 작업
- `TASKS.md`
  우선순위가 있는 작업 목록과 완료 기준
- `HARNESS.md`
  AI 개발용 검증 레일과 하네스 운영 기준
- `WORKFLOW.md`
  실제 프로젝트 진행 절차와 세션 운영 방식
- `.codex-start.txt`
  Codex 세션 시작용 프롬프트
- `docs/architecture.md`
  아키텍처 메모, 모듈 경계, 의사결정 기록
- `docs/exec-plans/`
  진행 중/완료된 실행 계획과 기술 부채 기록
- `docs/product-specs/`
  제품 요구사항과 사용자 흐름 문서
- `docs/references/`
  외부 도구 및 팀 참고 자료
- `docs/references/check-examples.md`
  스택별 검증 스크립트 예시
- `docs/generated/`
  자동 생성 자료
- `docs/QUALITY.md`, `docs/RELIABILITY.md`, `docs/SECURITY.md`
  품질, 신뢰성, 보안 기준
- `scripts/auto_codex_context.py`
  `CONTEXT.md`의 자동 생성 상태 블록을 갱신하는 스크립트
- `scripts/run.sh`, `scripts/run.bat`
  작업 시작 전 컨텍스트를 갱신하는 헬퍼 스크립트
- `scripts/check.sh`, `scripts/check.bat`, `scripts/check.py`
  표준 검증 하네스 진입점
- `scripts/project-intake.sh`, `scripts/project-intake.bat`, `scripts/project_intake.py`
  질문형 프로젝트 초기 설정 스크립트
- `scripts/create-project.sh`, `scripts/create-project.bat`, `scripts/create-project.ps1`
  이 템플릿으로 새 프로젝트를 생성하는 스캐폴딩 스크립트
- `scripts/create_project.py`
  새 프로젝트 생성의 실제 공통 로직
- `src/`
  애플리케이션 소스 코드
- `tests/`
  테스트 파일

## 가장 추천하는 시작 순서

실제 프로젝트에서는 아래 순서로 시작하는 것을 권장합니다.

1. `scripts/create-project.*`로 새 프로젝트 생성
2. `scripts/project-intake.*`로 질문에 답해 핵심 문서와 검증 스크립트 자동 작성
3. 생성된 `scripts/check.py`를 검토하고 필요하면 실제 스택에 맞게 보강
4. 첫 작업을 `TASKS.md`에 정리
5. 구현 시작

## 빠른 시작

1. 이 템플릿을 새 프로젝트 디렉터리로 복제합니다.
2. `project-intake` 스크립트로 질문에 답하면서 초기 정보를 자동으로 채웁니다.
3. 생성된 `scripts/check.py`를 검토하고 프로젝트에 맞는 검증 명령으로 보강합니다.
4. 새 세션을 시작하기 전에 아래 명령으로 컨텍스트를 갱신합니다.

```sh
python scripts/auto_codex_context.py
```

5. `.codex-start.txt`를 Codex 세션 시작 프롬프트로 사용합니다.
6. 코드 변경 후에는 아래 검증 하네스를 실행합니다.

```sh
python scripts/check.py
```

## 질문형 초기 설정

Windows:

```bat
scripts\project-intake.bat
```

macOS / Linux / WSL:

```sh
sh scripts/project-intake.sh
```

## 권장 세션 흐름

1. `README.md`, `WORKFLOW.md`, `AGENTS.md`, `AI_RULES.md`, `CONTEXT.md`, `TASKS.md`를 읽습니다.
2. `HARNESS.md`를 읽고 현재 검증 기준을 확인합니다.
3. 현재 요청과 직접 관련된 파일만 우선 확인합니다.
4. 요청된 변경을 구현합니다.
5. 코드 변경 후 관련 테스트나 검증을 수행합니다.
6. 테스트가 통과한 뒤에만 다음 단계로 진행합니다.
7. 같은 작업 안에서 관련 문서도 함께 수정합니다.
8. `python scripts/auto_codex_context.py`를 실행합니다.
9. 다음 세션이 바로 이어받을 수 있도록 `TASKS.md`, `CONTEXT.md`를 정리합니다.

## 권장 운영 규칙

- 변경은 작게 하고 빠르게 검증합니다.
- 코드 변경 후에는 테스트 통과 전 다음 단계로 넘어가지 않습니다.
- 표준 검증은 가능한 한 `scripts/check.*`로 모읍니다.
- 구조가 바뀌면 `docs/architecture.md`를 업데이트합니다.
- 우선순위가 바뀌면 `TASKS.md`를 바로 수정합니다.
- 세션 종료 전 `CONTEXT.md`가 인수인계 가능한 상태인지 확인합니다.

## 헬퍼 스크립트

Windows:

```bat
scripts\run.bat
```

macOS / Linux / WSL:

```sh
sh scripts/run.sh
```

검증 하네스 실행:

Windows:

```bat
scripts\check.bat
```

macOS / Linux / WSL:

```sh
sh scripts/check.sh
```

새 프로젝트 생성:

macOS / Linux / WSL:

```sh
sh scripts/create-project.sh my-app
```

Windows:

```bat
scripts\create-project.bat my-app
```

원격 URL을 자동으로 찾지 못하면 두 번째 인자로 템플릿 저장소 URL을 넘기거나 `TEMPLATE_REPO_URL` 환경 변수를 사용할 수 있습니다. Windows에서는 `.bat`이 내부적으로 `PowerShell` 스크립트를 호출합니다.
기본 설정에서는 프로젝트 생성 후 Codex를 자동 실행하지 않습니다. 생성이 끝나면 프로젝트 폴더로 이동해서 `codex`를 직접 실행하세요.
명시적으로 자동 실행을 켜고 싶다면 `CODEX_AUTOSTART=1` 환경 변수를 사용하면 됩니다.

## 기본 검증 프로필

현재 `scripts/check.py`는 Python/FastAPI 스타터 프로필로 채워져 있습니다.

기본 명령:

- `ruff check .`
- `mypy src`
- `pytest -q`

다른 스택을 사용할 경우 `docs/references/check-examples.md`를 참고해서 `scripts/check.py`를 바꾸면 됩니다.

## 하네스 엔지니어링 적용 방법

이 템플릿은 AI 개발에 하네스 엔지니어링을 적용하기 위해 다음 구조를 제공합니다.

1. `HARNESS.md`에 검증 원칙과 완료 기준을 기록
2. `scripts/check.*`를 표준 검증 진입점으로 사용
3. `AI_RULES.md`에 테스트 통과 전 다음 단계 금지 규칙 명시
4. `.codex-start.txt`에서 세션 시작 시 하네스 확인을 강제
5. `AGENTS.md`와 구조화된 `docs/`를 통해 필요한 지식을 분산 저장

## Windows 테스트 예시

상위 폴더에서 실행:

```powershell
cd C:\dev
C:\dev\codex-template\scripts\create-project.bat my-test-app https://github.com/leekangbok/codex-project-template.git
cd C:\dev\my-test-app
scripts\project-intake.bat
codex
```

## 유지보수 메모

이 템플릿은 의도적으로 기술 중립적으로 작성되어 있습니다.
실제 프로젝트에 맞게 커스터마이즈하되, 개요, 규칙, 문맥, 작업, 아키텍처의 역할 분리는 유지하는 것을 권장합니다.
