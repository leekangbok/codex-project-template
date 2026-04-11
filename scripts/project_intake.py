#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    print("프로젝트 초기 설정을 시작합니다.")
    print("질문에 답하면 핵심 문서를 자동으로 채웁니다.\n")

    project_name = ask("프로젝트명", ROOT.name)
    summary = ask("한 줄 요약", "아직 설명이 정리되지 않은 새 프로젝트")
    target_users = ask("대상 사용자", "내부 팀 또는 초기 사용자")
    problem = ask("해결하려는 핵심 문제", "핵심 문제 정의 필요")
    mvp_scope = ask("MVP 범위", "핵심 기능 1~2개부터 시작")
    out_of_scope = ask("초기 제외 범위", "고급 기능과 확장 요구사항은 제외")

    language = ask("사용 언어", "미정")
    framework = ask("프레임워크", "미정")
    package_manager = ask("패키지 매니저", "미정")
    test_tool = ask("테스트 도구", "미정")
    deploy_target = ask("배포 대상", "미정")

    install_cmd = ask("설치 명령", "미정")
    dev_cmd = ask("개발 실행 명령", "미정")
    test_cmd = ask("테스트 명령", "미정")
    lint_cmd = ask("린트 명령", "미정")
    build_cmd = ask("빌드 명령", "미정")

    first_feature = ask("가장 먼저 만들 기능", "첫 핵심 기능 정의 필요")
    main_risk = ask("현재 가장 큰 리스크", "요구사항과 구조가 아직 고정되지 않음")

    readme = f"""# {project_name}

{summary}

## 프로젝트 목적

- 대상 사용자: {target_users}
- 해결하려는 문제: {problem}
- MVP 범위: {mvp_scope}
- 제외 범위: {out_of_scope}

## 기술 스택

- 언어: {language}
- 프레임워크: {framework}
- 패키지 매니저: {package_manager}
- 테스트 도구: {test_tool}
- 배포 대상: {deploy_target}

## 표준 명령

- 설치 명령: `{install_cmd}`
- 개발 실행 명령: `{dev_cmd}`
- 테스트 명령: `{test_cmd}`
- 린트 명령: `{lint_cmd}`
- 빌드 명령: `{build_cmd}`

## 작업 원칙

- 코드 변경 후에는 관련 테스트나 검증을 수행합니다.
- 테스트 통과 전에는 다음 단계로 진행하지 않습니다.
- 구조가 바뀌면 문서를 함께 갱신합니다.

## 핵심 문서

- `AGENTS.md`: 에이전트용 지도
- `AI_RULES.md`: 작업 강제 규칙
- `HARNESS.md`: 검증 기준
- `CONTEXT.md`: 현재 상태
- `TASKS.md`: 우선순위 작업
- `WORKFLOW.md`: 진행 절차
"""

    context = f"""# 프로젝트 문맥

이 문서는 다음 세션이 2분 안에 현재 프로젝트 상태를 이해할 수 있도록 유지하는 문서입니다.

## 프로젝트 요약

- 프로젝트명: {project_name}
- 프로젝트 유형: {summary}
- 대상 사용자: {target_users}
- 현재 단계: 초기 프로젝트 설정 완료
- 목표: {problem}

## 현재 상태

- 기본 프로젝트 문서가 초기화됨
- 첫 구현 전 요구사항과 구조가 정리된 상태
- 검증 하네스는 프로젝트 명령 기준으로 추가 설정 필요

## 현재 결정 사항

- 언어: {language}
- 프레임워크: {framework}
- 테스트 도구: {test_tool}
- 배포 대상: {deploy_target}

## 현재 리스크

- {main_risk}

## 다음 권장 작업

1. {first_feature} 구현
2. `scripts/check.py`에 실제 검증 명령 반영
3. 첫 테스트 추가
4. 아키텍처 세부화

## 자동 생성 상태

<!-- AUTO-GENERATED-START -->
이 블록은 `python scripts/auto_codex_context.py` 실행 시 갱신됩니다.
<!-- AUTO-GENERATED-END -->

## 세션 메모

- intake 스크립트로 초기 프로젝트 정보가 입력됨
- 프로젝트명: {project_name}
"""

    tasks = f"""# 작업 목록

## 지금

- [ ] {first_feature} 구현하기
- [ ] `scripts/check.py`에 실제 lint/test/typecheck/build 명령 채우기
- [ ] 첫 테스트 추가하기
- [ ] `docs/architecture.md`를 실제 구조로 구체화하기

## 다음

- [ ] 주요 사용자 흐름 문서화하기
- [ ] 실행/배포 절차 확정하기
- [ ] 초기 리스크 완화하기

## 이후

- [ ] CI 구성 추가하기
- [ ] 기술 부채 트래킹 시작하기
- [ ] 운영 지표와 관측성 정리하기

## 완료 기준

- [ ] 코드와 문서가 함께 업데이트되었다
- [ ] 테스트 또는 검증이 통과했다
- [ ] `CONTEXT.md`가 최신 상태다
- [ ] 다음 작업이 명확하다
"""

    architecture = f"""# 아키텍처 메모

## 1. 시스템 요약

- 프로젝트명: {project_name}
- 프로젝트 유형: {summary}
- 핵심 목표: {problem}
- 주요 사용자: {target_users}

## 2. 기술 스택

- 언어: {language}
- 프레임워크: {framework}
- 패키지 매니저: {package_manager}
- 테스트 도구: {test_tool}
- 배포 대상: {deploy_target}

## 3. 초기 구조 방향

- 첫 구현 대상: {first_feature}
- MVP 범위: {mvp_scope}
- 제외 범위: {out_of_scope}

## 4. 결정 로그

### Decision 001: Initial Stack

- Status: Accepted
- Context: 초기 프로젝트 설정
- Decision: {language} / {framework}
- Consequence: 관련 명령과 검증 하네스를 함께 유지해야 함
"""

    harness = f"""# 하네스 엔지니어링 가이드

## 목적

- 코드 변경 후 검증이 통과할 때만 다음 단계로 진행
- AI와 사람이 같은 완료 기준을 공유
- 회귀를 빠르게 발견

## 현재 프로젝트 검증 기준

- 테스트 명령: `{test_cmd}`
- 린트 명령: `{lint_cmd}`
- 빌드 명령: `{build_cmd}`
- 개발 실행 명령: `{dev_cmd}`

## 기본 규칙

1. 코드가 바뀌면 `scripts/check.py` 또는 관련 검증을 실행합니다.
2. 검증이 실패하면 수정 후 다시 검증합니다.
3. 검증 통과 전에는 다음 단계로 진행하지 않습니다.
4. 검증 명령이 바뀌면 `README.md`와 이 문서를 함께 갱신합니다.

## 현재 우선 검증 대상

- 첫 기능: {first_feature}
- 가장 큰 리스크: {main_risk}

## 다음 할 일

- `scripts/check.py`에 `{test_cmd}`, `{lint_cmd}`, `{build_cmd}` 반영
- 필요하면 타입체크와 통합 테스트 추가
"""

    write(ROOT / "README.md", readme)
    write(ROOT / "CONTEXT.md", context)
    write(ROOT / "TASKS.md", tasks)
    write(ROOT / "docs" / "architecture.md", architecture)
    write(ROOT / "HARNESS.md", harness)

    print("\n핵심 문서를 업데이트했습니다.")
    print("- README.md")
    print("- CONTEXT.md")
    print("- TASKS.md")
    print("- docs/architecture.md")
    print("- HARNESS.md")
    print("\n다음 권장 명령:")
    print("python scripts/auto_codex_context.py")
    print("python scripts/check.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
