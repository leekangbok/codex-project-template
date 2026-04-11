---
name: refactoring-expert
description: Expertise in improving code structure, readability, and maintainability without changing external behavior. Use when code is messy, has high complexity, duplication, or technical debt.
---

# Refactoring Expert

## Goals
- Improve code quality, maintainability, and scalability.
- Reduce technical debt and cognitive load.
- Ensure zero change in external behavior (behavioral parity).

## Principles
- **Small Steps**: Make incremental changes. Run tests after each small refactor.
- **Red-Green-Refactor**: Ideally, have tests in place before refactoring.
- **DRY (Don't Repeat Yourself)**: Eliminate duplication.
- **SOLID Principles**: Apply Single Responsibility, Open/Closed, etc.
- **KISS (Keep It Simple, Stupid)**: Favor simplicity over clever abstractions.

## Patterns
- **Extract Method/Function**: Break down large, complex functions.
- **Rename Variable/Function**: Use intention-revealing names.
- **Replace Conditional with Polymorphism**: Simplify complex if-else or switch blocks.
- **Introduce Parameter Object**: Group related parameters into a single object/class.
- **Encapsulate Field**: Restrict direct access to data members.

## Workflow
1. **Analyze**: Identify code smells (long methods, large classes, duplication).
2. **Verify**: Ensure existing tests pass. If no tests, write basic regression tests.
3. **Refactor**: Apply a specific pattern (e.g., Extract Method).
4. **Test**: Run tests to ensure no regressions.
5. **Clean Up**: Remove any orphaned code or comments created by the refactor.
6. **Repeat**: Move to the next smallest unit of improvement.

## Anti-Patterns to Avoid
- **Speculative Generality**: Don't add "hooks" or "flexibility" for future needs that aren't here yet.
- **Big Bang Refactoring**: Avoid changing everything at once.
- **Gold Plating**: Don't refactor code that is working fine and won't be touched again.
