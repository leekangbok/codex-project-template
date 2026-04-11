#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    try:
        value = input(f"{prompt}{suffix}: ").strip()
    except EOFError:
        print("\n입력이 중단되었습니다. 이 스크립트는 대화형 터미널에서 실행해야 합니다.")
        raise SystemExit(1)
    return value or default


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def infer_check_steps(
    language: str,
    framework: str,
    package_manager: str,
    test_tool: str,
) -> list[tuple[str, list[str]]]:
    lang = language.lower()
    fw = framework.lower()
    pkg = package_manager.lower()
    test = test_tool.lower()

    if "python" in lang or "fastapi" in fw or "pytest" in test:
        return [
            ("lint", ["ruff", "check", "."]),
            ("typecheck", ["mypy", "src"]),
            ("test", ["pytest", "-q"]),
        ]

    if "node" in lang or "typescript" in lang or "next" in fw:
        runner = "pnpm" if "pnpm" in pkg else "yarn" if "yarn" in pkg else "npm"
        if runner == "yarn":
            return [
                ("lint", ["yarn", "lint"]),
                ("typecheck", ["yarn", "typecheck"]),
                ("test", ["yarn", "test"]),
                ("build", ["yarn", "build"]),
            ]
        return [
            ("lint", [runner, "run", "lint"]),
            ("typecheck", [runner, "run", "typecheck"]),
            ("test", [runner, "run", "test"]),
            ("build", [runner, "run", "build"]),
        ]

    if "rust" in lang:
        return [
            ("fmt", ["cargo", "fmt", "--check"]),
            ("lint", ["cargo", "clippy", "--", "-D", "warnings"]),
            ("test", ["cargo", "test"]),
        ]

    if lang == "go" or "golang" in lang:
        return [
            ("fmt", ["gofmt", "-w", "."]),
            ("test", ["go", "test", "./..."]),
        ]

    return []


def render_check_script(
    language: str,
    framework: str,
    package_manager: str,
    test_tool: str,
) -> str:
    steps = infer_check_steps(language, framework, package_manager, test_tool)
    if steps:
        rendered_steps = "[\n" + "".join(
            f'        ("{name}", {command}),\n' for name, command in steps
        ) + "    ]"
    else:
        rendered_steps = "[]"

    return f"""#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(name: str, command: list[str]) -> bool:
    print(f"[check] {{name}}: {{' '.join(command)}}")
    try:
        subprocess.run(command, cwd=ROOT, check=True)
    except FileNotFoundError:
        print(f"[check] skipped: command not found for '{{name}}'")
        return False
    except subprocess.CalledProcessError as exc:
        print(f"[check] failed: {{name}} (exit code {{exc.returncode}})")
        raise
    else:
        print(f"[check] passed: {{name}}")
        return True


def main() -> int:
    print("표준 검증 하네스를 시작합니다.")
    print("현재 프로젝트 기준 스택: {language} / {framework}")
    print("다른 스택 예시는 docs/references/check-examples.md 를 참고하세요.")

    steps: list[tuple[str, list[str]]] = {rendered_steps}

    if not steps:
        print("[check] configured commands: none")
        print("[check] TODO: lint/test/typecheck/build 명령을 현재 프로젝트에 맞게 추가하세요.")
        return 0

    any_executed = False
    for name, command in steps:
        if command and shutil.which(command[0]):
            any_executed = True
        run_step(name, command)

    if not any_executed:
        print("[check] warning: no executable commands were found in the current environment")
        print("[check] 현재 프로젝트에 맞게 steps를 수정하거나 필요한 도구를 설치하세요.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""


def main() -> int:
    print("프로젝트 초기 설정을 시작합니다.")
    print("질문에 답하면 핵심 문서를 현재 프로젝트에 맞게 자동으로 채웁니다.\n")

    project_name = ask("프로젝트명", ROOT.name)
    summary = ask("한 줄 요약", "아직 설명이 정리되지 않은 신규 프로젝트")
    target_users = ask("주요 사용자", "내부 팀 또는 초기 사용자")
    problem = ask("해결하려는 문제", "문제 정의가 더 필요합니다")
    mvp_scope = ask("MVP 범위", "핵심 기능 1~2개부터 시작")
    out_of_scope = ask("초기 제외 범위", "고급 기능과 확장 요구사항은 제외")

    language = ask("사용 언어", "Python")
    framework = ask("프레임워크", "FastAPI")
    package_manager = ask("패키지 매니저", "pip")
    test_tool = ask("테스트 도구", "pytest")
    deploy_target = ask("배포 대상", "미정")

    install_cmd = ask("설치 명령", "pip install -r requirements.txt")
    dev_cmd = ask("개발 실행 명령", "uvicorn src.main:app --reload")
    test_cmd = ask("테스트 명령", "pytest -q")
    lint_cmd = ask("린트 명령", "ruff check .")
    build_cmd = ask("빌드 명령", "미정")

    first_feature = ask("가장 먼저 만들 기능", "첫 핵심 기능 정의 필요")
    main_risk = ask("현재 가장 큰 리스크", "요구사항과 구조가 아직 고정되지 않음")

    readme = f"""# {project_name}

{summary}

## 프로젝트 목적

- 주요 사용자: {target_users}
- 해결하려는 문제: {problem}
- MVP 범위: {mvp_scope}
- 초기 제외 범위: {out_of_scope}

## 기술 스택

- 언어: {language}
- 프레임워크: {framework}
- 패키지 매니저: {package_manager}
- 테스트 도구: {test_tool}
- 배포 대상: {deploy_target}

## 주요 명령

- 설치 명령: `{install_cmd}`
- 개발 실행 명령: `{dev_cmd}`
- 테스트 명령: `{test_cmd}`
- 린트 명령: `{lint_cmd}`
- 빌드 명령: `{build_cmd}`

## 작업 원칙

- 코드 변경 전후로 관련 문서를 함께 확인합니다.
- 코드 변경 후에는 테스트나 검증을 반드시 수행합니다.
- 테스트 통과 전에는 다음 단계로 진행하지 않습니다.
- 구조가 바뀌면 문서도 같은 작업 안에서 갱신합니다.

## 핵심 문서

- `AGENTS.md`: 에이전트를 위한 지도
- `AI_RULES.md`: 작업 강제 규칙
- `HARNESS.md`: 검증 기준과 완료 조건
- `CONTEXT.md`: 현재 상태와 인수인계 메모
- `TASKS.md`: 우선순위 작업 목록
- `WORKFLOW.md`: 실제 운영 절차
"""

    context = f"""# 프로젝트 문맥

이 문서는 다음 세션이 2분 안에 현재 프로젝트 상태를 이해하도록 돕는 요약 문서입니다.

## 프로젝트 요약

- 프로젝트명: {project_name}
- 한 줄 요약: {summary}
- 주요 사용자: {target_users}
- 현재 단계: 초기 설정 완료
- 해결하려는 문제: {problem}

## 현재 상태

- 핵심 문서가 프로젝트 기준으로 초기화되었습니다.
- 첫 구현 전 요구사항과 구조를 정리하는 단계입니다.
- 검증 하네스는 `scripts/check.py`를 중심으로 운영합니다.

## 현재 결정 사항

- 언어: {language}
- 프레임워크: {framework}
- 테스트 도구: {test_tool}
- 배포 대상: {deploy_target}

## 현재 리스크

- {main_risk}

## 다음 권장 작업

1. {first_feature} 구현
2. `scripts/check.py` 실행으로 검증 흐름 확인
3. 첫 테스트 추가
4. `docs/architecture.md` 구체화

## 자동 생성 상태

<!-- AUTO-GENERATED-START -->
이 블록은 `python scripts/auto_codex_context.py` 실행 후 갱신됩니다.
<!-- AUTO-GENERATED-END -->

## 세션 메모

- `project-intake` 스크립트로 초기 프로젝트 정보를 입력했습니다.
- 프로젝트명: {project_name}
"""

    tasks = f"""# 작업 목록

## 지금

- [ ] {first_feature} 구현하기
- [ ] `scripts/check.py` 검증 흐름 확인하기
- [ ] 첫 테스트 추가하기
- [ ] `docs/architecture.md`를 실제 구조로 구체화하기

## 다음

- [ ] 주요 사용자 흐름 문서화하기
- [ ] 실행 및 배포 절차 정리하기
- [ ] 초기 리스크 완화하기

## 이후

- [ ] CI 구성 추가하기
- [ ] 기술 부채 추적 시작하기
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
- 한 줄 요약: {summary}
- 해결하려는 문제: {problem}
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
- Consequence: 관련 명령과 검증 하네스를 같은 기준으로 유지해야 합니다.
"""

    harness = f"""# 하네스 엔지니어링 가이드

## 목적

- 코드 변경은 검증 통과 이후에만 완료로 간주합니다.
- AI와 사람이 같은 완료 기준을 공유합니다.
- 오류를 빠르게 발견하고 회귀를 줄입니다.

## 현재 프로젝트 검증 기준

- 테스트 명령: `{test_cmd}`
- 린트 명령: `{lint_cmd}`
- 빌드 명령: `{build_cmd}`
- 개발 실행 명령: `{dev_cmd}`

## 기본 규칙

1. 코드가 바뀌면 `scripts/check.py` 또는 관련 검증 명령을 실행합니다.
2. 검증이 실패하면 수정 후 다시 검증합니다.
3. 검증 통과 전에는 다음 단계로 진행하지 않습니다.
4. 검증 명령이 바뀌면 `README.md`와 관련 문서를 함께 갱신합니다.

## 현재 우선 검증 대상

- 첫 기능: {first_feature}
- 현재 리스크: {main_risk}

## 다음 보강 항목

- `scripts/check.py`를 실제 프로젝트 명령과 완전히 맞추기
- 필요하면 통합 테스트나 스모크 테스트 추가하기
"""

    write(ROOT / "README.md", readme)
    write(ROOT / "CONTEXT.md", context)
    write(ROOT / "TASKS.md", tasks)
    write(ROOT / "docs" / "architecture.md", architecture)
    write(ROOT / "HARNESS.md", harness)
    write(
        ROOT / "scripts" / "check.py",
        render_check_script(language, framework, package_manager, test_tool),
    )

    print("\n다음 문서를 업데이트했습니다.")
    print("- README.md")
    print("- CONTEXT.md")
    print("- TASKS.md")
    print("- docs/architecture.md")
    print("- HARNESS.md")
    print("- scripts/check.py")
    print("\n다음 권장 명령:")
    print("python scripts/auto_codex_context.py")
    print("python scripts/check.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
