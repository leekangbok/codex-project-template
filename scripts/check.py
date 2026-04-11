#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_step(name: str, command: list[str]) -> bool:
    print(f"[check] {name}: {' '.join(command)}")
    try:
        subprocess.run(command, cwd=ROOT, check=True)
    except FileNotFoundError:
        print(f"[check] skipped: command not found for '{name}'")
        return False
    except subprocess.CalledProcessError as exc:
        print(f"[check] failed: {name} (exit code {exc.returncode})")
        raise
    else:
        print(f"[check] passed: {name}")
        return True


def main() -> int:
    print("표준 검증 하네스를 시작합니다.")
    print("기본 스타터 프로필은 Python/FastAPI 기준입니다.")
    print("다른 스택 예시는 docs/references/check-examples.md 를 참고하세요.")

    # 기본 스타터 프로필: Python / FastAPI
    # 다른 스택을 사용할 경우 아래 steps를 프로젝트에 맞게 교체하세요.
    steps: list[tuple[str, list[str]]] = [
        ("lint", ["ruff", "check", "."]),
        ("typecheck", ["mypy", "src"]),
        ("test", ["pytest", "-q"]),
    ]

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
