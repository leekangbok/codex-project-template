#!/usr/bin/env python3
from __future__ import annotations

import os
import stat
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], *, cwd: Path | None = None, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        input=input_text,
        text=True,
        encoding="utf-8",
        check=True,
    )


def optional_output(command: list[str], *, cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd) if cwd else None,
            text=True,
            check=True,
            capture_output=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def _handle_remove_readonly(func, path, _exc_info) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_tree(path: Path) -> None:
    shutil.rmtree(path, onexc=_handle_remove_readonly)


def resolve_template_repo(explicit_repo: str | None) -> str:
    if explicit_repo:
        return explicit_repo

    env_repo = os.environ.get("TEMPLATE_REPO_URL", "").strip()
    if env_repo:
        return env_repo

    return optional_output(["git", "-C", str(ROOT), "remote", "get-url", "origin"])


def rewrite_readme(project_dir: Path, project_name: str) -> None:
    readme = project_dir / "README.md"
    if not readme.exists():
        return

    lines = readme.read_text(encoding="utf-8").splitlines()
    if lines:
        lines[0] = f"# {project_name}"
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_context(project_dir: Path, project_name: str) -> None:
    context = f"""# 프로젝트 문맥

이 문서는 다음 세션이 2분 안에 현재 프로젝트 상태를 이해할 수 있도록 유지하는 문서입니다.

## 프로젝트 요약

- 프로젝트 유형: 신규 프로젝트
- 현재 단계: 초기 생성 완료
- 목표: {project_name} 프로젝트 시작
- 상태: 템플릿에서 생성되었고 실제 요구사항 정리가 아직 필요함

## 현재 존재하는 것

- 기본 운영 문서: `README.md`, `AI_RULES.md`, `CONTEXT.md`, `TASKS.md`
- 세션 시작 프롬프트: `.codex-start.txt`
- 아키텍처 문서: `docs/architecture.md`
- 컨텍스트 갱신 스크립트: `scripts/auto_codex_context.py`
- 실행 헬퍼 스크립트: `scripts/run.sh`, `scripts/run.bat`

## 아직 비어 있는 정보

- 구체적인 요구사항
- 기술 스택
- 표준 실행 및 테스트 명령
- MVP 범위

## 현재 리스크

- 요구사항과 우선순위가 아직 확정되지 않았음
- 첫 구현 파일과 첫 테스트 파일이 아직 없음

## 다음 권장 작업

1. 요구사항을 정리합니다.
2. 기술 스택을 결정합니다.
3. 첫 기능 범위를 정의합니다.
4. 첫 구현 파일과 첫 테스트 파일을 추가합니다.

## 자동 생성 상태

<!-- AUTO-GENERATED-START -->
이 블록은 `python scripts/auto_codex_context.py` 실행 시 갱신됩니다.
<!-- AUTO-GENERATED-END -->

## 세션 메모

- 템플릿 저장소에서 새 프로젝트가 생성됨
- 프로젝트명: {project_name}
"""
    (project_dir / "CONTEXT.md").write_text(context, encoding="utf-8")


def write_tasks(project_dir: Path, project_name: str) -> None:
    tasks = f"""# 작업 목록

이 파일은 다음에 해야 할 실제 작업에 집중해야 합니다.

## 지금

- [ ] {project_name}의 요구사항 정리하기
- [ ] 기술 스택 결정하기
- [ ] 첫 기능 범위 정의하기
- [ ] `docs/architecture.md`를 실제 구조로 갱신하기

## 다음

- [ ] `src/` 아래 첫 구현 파일 추가하기
- [ ] `tests/` 아래 첫 테스트 파일 추가하기
- [ ] 실행 및 테스트 명령 문서화하기

## 이후

- [ ] 린트/포맷터 설정 추가하기
- [ ] CI 구성 추가하기
- [ ] 배포 전략 문서화하기
"""
    (project_dir / "TASKS.md").write_text(tasks, encoding="utf-8")


def maybe_commit(project_dir: Path) -> None:
    git_name = optional_output(["git", "config", "user.name"], cwd=project_dir)
    git_email = optional_output(["git", "config", "user.email"], cwd=project_dir)
    if not git_name or not git_email:
        print("Git user.name 또는 user.email이 설정되지 않아 첫 커밋은 건너뜁니다.")
        return

    run(["git", "commit", "-m", "Initial project setup from template"], cwd=project_dir)
    print("첫 커밋을 생성했습니다.")


def maybe_run_codex(project_dir: Path) -> None:
    autostart = os.environ.get("CODEX_AUTOSTART", "0").strip()
    if autostart not in {"1", "true", "True", "yes", "on"}:
        print("기본 설정에서는 Codex 자동 실행을 하지 않습니다.")
        print(f"필요하면 프로젝트 폴더로 이동한 뒤 수동으로 실행하세요: cd {project_dir} && codex")
        return

    codex_path = shutil.which("codex")
    if not codex_path:
        print("codex 명령을 찾지 못했습니다. 필요하면 프로젝트 폴더에서 수동으로 실행하세요.")
        return

    prompt = (project_dir / ".codex-start.txt").read_text(encoding="utf-8-sig")
    print("Codex 세션을 시작합니다.")
    try:
        run([codex_path], cwd=project_dir, input_text=prompt)
    except Exception as exc:
        print(f"Codex 자동 실행에 실패했습니다: {exc}")
        print("프로젝트 생성은 완료되었으니, 프로젝트 폴더에서 codex를 수동으로 실행하세요.")


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("프로젝트 이름을 입력하세요.")
        print("사용법: create-project <project-name> [template-repo-url]")
        return 1

    project_name = sys.argv[1].strip()
    template_repo = resolve_template_repo(sys.argv[2].strip() if len(sys.argv) > 2 else None)

    if not template_repo:
        print("템플릿 저장소 URL을 찾을 수 없습니다.")
        print("두 번째 인자로 URL을 넘기거나 TEMPLATE_REPO_URL 환경 변수를 설정하세요.")
        return 1

    project_dir = Path(project_name).resolve()
    if project_dir.exists():
        print(f"대상 경로가 이미 존재합니다: {project_dir}")
        return 1

    print(f"프로젝트 생성 시작: {project_name}")
    print(f"템플릿 저장소: {template_repo}")

    run(["git", "clone", template_repo, project_name], cwd=Path.cwd())
    remove_tree(project_dir / ".git")
    run(["git", "init", "-b", "main"], cwd=project_dir)

    rewrite_readme(project_dir, project_name)
    write_context(project_dir, project_name)
    write_tasks(project_dir, project_name)

    run([sys.executable, "scripts/auto_codex_context.py"], cwd=project_dir)
    run(["git", "add", "."], cwd=project_dir)
    maybe_commit(project_dir)

    print(f"프로젝트 생성 완료: {project_name}")
    maybe_run_codex(project_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
