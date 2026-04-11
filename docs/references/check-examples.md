# 검증 스크립트 예시

이 문서는 `scripts/check.py`에 어떤 명령을 넣으면 좋은지 스택별 예시를 제공합니다.

## Python 예시

```python
steps = [
    ("lint", ["ruff", "check", "."]),
    ("format-check", ["ruff", "format", "--check", "."]),
    ("test", ["pytest", "-q"]),
]
```

## FastAPI / Python 예시

```python
steps = [
    ("lint", ["ruff", "check", "."]),
    ("typecheck", ["mypy", "src"]),
    ("test", ["pytest", "-q"]),
]
```

## Node.js / TypeScript 예시

```python
steps = [
    ("lint", ["npm", "run", "lint"]),
    ("typecheck", ["npm", "run", "typecheck"]),
    ("test", ["npm", "run", "test"]),
    ("build", ["npm", "run", "build"]),
]
```

## Next.js 예시

```python
steps = [
    ("lint", ["npm", "run", "lint"]),
    ("typecheck", ["npx", "tsc", "--noEmit"]),
    ("test", ["npm", "run", "test"]),
    ("build", ["npm", "run", "build"]),
]
```

## Rust 예시

```python
steps = [
    ("fmt", ["cargo", "fmt", "--check"]),
    ("lint", ["cargo", "clippy", "--", "-D", "warnings"]),
    ("test", ["cargo", "test"]),
]
```

## Go 예시

```python
steps = [
    ("fmt", ["gofmt", "-w", "."]),
    ("test", ["go", "test", "./..."]),
]
```

## 권장 팁

- 가장 빠른 검증부터 앞에 둡니다.
- 실패 가능성이 높은 검증을 먼저 둡니다.
- CI에서 돌리는 명령과 최대한 맞춥니다.
- 새 명령을 추가하면 `HARNESS.md`와 `README.md`도 함께 갱신합니다.
