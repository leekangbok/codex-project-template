#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def ask(prompt: str, default: str = "", description: str = "") -> str:
    if description:
        print(f"\n[도움말] {description}")
    suffix = f" [{default}]" if default else ""
    try:
        value = input(f"   {prompt}{suffix}: ").strip()
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

    project_name = ask(
        "프로젝트명",
        ROOT.name,
        "프로젝트를 고유하게 식별하는 이름입니다. 폴더명, 설정 데이터, 문서 제목의 기준이 됩니다. (예: my-awesome-app, data-cruncher-cli)",
    )
    summary = ask(
        "한 줄 요약",
        "아직 설명이 정리되지 않은 신규 프로젝트",
        "프로젝트의 존재 이유를 빠르게 전달합니다. 협업자나 AI가 3초 안에 파악할 수 있게 돕습니다. (예: 저지연 분산 로그 수집기, 개인용 가계부)",
    )
    target_users = ask(
        "주요 사용자",
        "내부 팀 또는 초기 사용자",
        "제품을 실제로 사용하는 사람이나 시스템입니다. 타겟에 따라 에러 메시지나 UI 설계 방향이 결정됩니다. (예: 사내 개발팀, 일반 사용자)",
    )
    problem = ask(
        "해결하려는 문제",
        "문제 정의가 더 필요합니다",
        "이 프로젝트가 해결하려는 핵심 통증(Pain point)입니다. 모든 기능 추가 여부의 기준이 됩니다. (예: 기기 간 데이터 동기화 속도 저하, 수동 영수증 처리의 번거로움)",
    )
    mvp_scope = ask(
        "MVP 범위",
        "핵심 기능 1~2개부터 시작",
        "가장 먼저 완성해야 할 핵심 기능군입니다. 빠르게 실제 가치를 검증하기 위한 최소 범위입니다. (예: 로그인 및 메모 작성 서비스, CSV 차트 시각화 로직)",
    )
    out_of_scope = ask(
        "초기 제외 범위",
        "고급 기능과 확장 요구사항은 제외",
        "초기 단계에서 의도적으로 배제할 기능입니다. 일정 지연과 설계 복잡도를 방지합니다. (예: 소셜 로그인, 모바일 앱 지원, 다국어 설정)",
    )

    language = ask(
        "사용 언어",
        "Python",
        "프로젝트의 주력 프로그래밍 언어입니다. AI의 코드 작성 스타일과 환경 구축의 기준이 됩니다. (예: Python, Rust, Go, TypeScript)",
    )
    framework = ask(
        "프레임워크",
        "FastAPI",
        "사용할 주력 프레임워크입니다. 시스템 아키텍처와 라이브러리 선택에 영향을 줍니다. (예: FastAPI, Axum, Gin, Next.js)",
    )
    package_manager = ask(
        "패키지 매니저",
        "pip",
        "라이브러리와 의존성을 관리할 도구입니다. (예: pip, npm, pnpm, cargo, go mod)",
    )
    test_tool = ask(
        "테스트 도구",
        "pytest",
        "코드의 품질을 검증할 테스트 프레임워크입니다. (예: pytest, vitest, jest, go test, cargo test)",
    )
    deploy_target = ask(
        "배포 대상",
        "미정",
        "최종적으로 제품이 실행될 환경입니다. 인프라 설정의 기준이 됩니다. (예: AWS Lambda, Vercel, Docker, On-premise)",
    )

    install_cmd = ask(
        "설치 명령",
        "pip install -r requirements.txt",
        "신규 참여자가 개발 환경을 구축하기 위해 실행할 표준 명령입니다. (예: pip install -r requirements.txt, npm install)",
    )
    dev_cmd = ask(
        "개발 실행 명령",
        "uvicorn src.main:app --reload",
        "로컬 환경에서 개발 서버를 띄우거나 앱을 실행할 명령입니다. (예: uvicorn src.main:app --reload, npm run dev)",
    )
    test_cmd = ask(
        "테스트 명령",
        "pytest -q",
        "전체 테스트를 실행하는 표준 명령입니다. (예: pytest -q, npm test, cargo test)",
    )
    lint_cmd = ask(
        "린트 명령",
        "ruff check .",
        "코드 스타일과 문법 오류를 체크하는 명령입니다. (예: ruff check ., eslint ., cargo clippy)",
    )
    build_cmd = ask(
        "빌드 명령",
        "미정",
        "배포를 위해 제품을 빌드하거나 컴파일하는 명령입니다. (예: docker build -t my-app ., npm run build)",
    )

    first_feature = ask(
        "가장 먼저 만들 기능",
        "첫 핵심 기능 정의 필요",
        "지금 바로 구현을 시작할 구체적인 첫 번째 핵심 조각입니다. '무엇부터 할까' 고민을 즉시 해결합니다. (예: DB 연결 설정, 기본 레이아웃 제작)",
    )
    main_risk = ask(
        "현재 가장 큰 리스크",
        "요구사항과 구조가 아직 고정되지 않음",
        "성공을 방해할 수 있는 위협 요소입니다. 미리 인지하면 대응책을 세우거나 설계를 보강할 수 있습니다. (예: 외부 API 속도 불안정, 기술 숙련도 부족)",
    )

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
