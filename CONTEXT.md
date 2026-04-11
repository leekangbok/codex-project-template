# 프로젝트 문맥

이 문서는 다음 세션이 2분 안에 현재 프로젝트 상태를 이해할 수 있도록 유지하는 문서입니다.

## 프로젝트 요약

- 프로젝트 유형: Codex CLI 개발 템플릿
- 현재 단계: 초기 템플릿 구성 완료
- 목표: Codex 기반 새 프로젝트를 시작할 때 재사용 가능한 기준 구조 제공
- 상태: 문서와 헬퍼 스크립트는 준비되었지만 실제 제품 코드는 아직 없음

## 현재 존재하는 것

- 핵심 문서: `README.md`, `AI_RULES.md`, `CONTEXT.md`, `TASKS.md`
- 에이전트 지도: `AGENTS.md`
- 하네스 문서: `HARNESS.md`
- 세션 시작 프롬프트: `.codex-start.txt`
- 아키텍처 문서: `docs/architecture.md`
- 구조화된 지식 베이스: `docs/exec-plans/`, `docs/product-specs/`, `docs/references/`, `docs/generated/`
- 컨텍스트 갱신 스크립트: `scripts/auto_codex_context.py`
- 표준 검증 하네스: `scripts/check.sh`, `scripts/check.bat`, `scripts/check.py`
- 실행 헬퍼 스크립트: `scripts/run.sh`, `scripts/run.bat`
- 프로젝트 생성 스크립트: `scripts/create-project.sh`, `scripts/create-project.bat`, `scripts/create-project.ps1`
- 플레이스홀더 코드 및 테스트 디렉터리: `src/`, `tests/`

## 아직 비어 있는 정보

- 실제 프로젝트명
- 제품 목표
- 대상 사용자
- 기술 스택
- 표준 실행 및 테스트 명령
- MVP 범위

## 현재 리스크

- 실제 프로젝트 메타데이터가 아직 채워지지 않았음
- `src/`, `tests/`는 아직 플레이스홀더 상태임
- 표준 명령이 아직 확정되지 않았음
- 템플릿 생성 스크립트 추가 후 사용 문서를 함께 유지해야 함
- `scripts/check.py`에 실제 프로젝트 검증 명령이 아직 채워지지 않았음

## 다음 권장 작업

1. `README.md`에 실제 프로젝트 정보를 채웁니다.
2. 기본 아키텍처 메모를 실제 스택과 경계로 교체합니다.
3. `TASKS.md`의 예시 작업을 실제 우선순위로 교체합니다.
4. `HARNESS.md`와 `scripts/check.py`에 실제 검증 기준을 채웁니다.
5. 첫 구현 파일과 첫 테스트 파일을 추가합니다.

## 자동 생성 상태

<!-- AUTO-GENERATED-START -->
이 블록은 `python scripts/auto_codex_context.py` 실행 시 갱신됩니다.

- 마지막 갱신 시각: 2026-04-11 07:34 UTC
- `README.md` 존재 여부: yes
- `docs/architecture.md` 존재 여부: yes
- `src/` 파일 수: 2
- `tests/` 파일 수: 2
- 완료된 작업 수: 0/19
<!-- AUTO-GENERATED-END -->

## 세션 메모

- 위 요약은 가능한 한 빨리 실제 프로젝트 정보로 교체합니다.
- 구조나 상태가 바뀌면 자동 생성 블록을 다시 갱신합니다.
