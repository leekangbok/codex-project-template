---
name: git-conventions
description: Guidelines for managing Git branches, commit messages, and workflows. Use to ensure a clean, understandable, and collaborative version control history.
---

# Git Conventions

## Branch Naming
- **feat/**: New features (e.g., `feat/user-auth`)
- **fix/**: Bug fixes (e.g., `fix/header-alignment`)
- **docs/**: Documentation changes (e.g., `docs/api-ref`)
- **refactor/**: Code refactoring (e.g., `refactor/scheduler`)
- **test/**: Adding or improving tests (e.g., `test/payment-flow`)

## Commit Message Format
Follow the **Conventional Commits** specification:
`<type>[optional scope]: <description>`

Example:
`feat(auth): implement JWT token verification`

## Guidelines
- **Commit Often, Perfect Later**: Make small, logical commits. Use `git commit --amend` or interactive rebase to clean up before pushing.
- **Atomic Commits**: One commit should do ONE thing.
- **Clear Descriptions**: The description should be imperative ("Add feature" not "Added feature") and concise.
- **No Large File Check-ins**: Use `.gitignore` to avoid checking in build artifiacts, Node modules, or large binaries.
- **Rebase vs Merge**: Prefer rebasing your feature branch on `main` before merging to keep a linear history.

## Workflow (GitHub Flow)
1. Fork/Clone the repo.
2. Create a specific branch for your work.
3. Make changes and commit with descriptive messages.
4. Push the branch to the remote.
5. Open a Pull Request (PR) for review.
6. Once approved and tested, merge the branch.
