---
name: code-review-checklist
description: A comprehensive checklist for conducting high-quality code reviews. Use during review tasks to ensure consistency, security, and performance.
---

# Code Review Checklist

## General
- [ ] Is the code readable and well-structured?
- [ ] Are variable and function names intention-revealing?
- [ ] Are there any obvious logic errors or edge cases missed?
- [ ] Is the code DRY (no unnecessary duplication)?
- [ ] Does it follow the project's established style and conventions?

## Functionality
- [ ] Does the code actually solve the problem it's intended to?
- [ ] Are all requirements from the task met?
- [ ] Are units/types correct (e.g., bits vs bytes, ms vs s)?

## Security
- [ ] Is user input sanitized/validated?
- [ ] Are there any potential SQL injection, XSS, or CSRF vulnerabilities?
- [ ] Are sensitive keys or credentials hardcoded?
- [ ] Are permissions checked properly?

## Performance
- [ ] Are there any obvious performance bottlenecks (e.g., O(N^2) loops)?
- [ ] Are database queries optimized?
- [ ] Is memory usage efficient?

## Error Handling
- [ ] Are exceptions caught and handled appropriately?
- [ ] Are error messages informative but not leaking sensitive data?
- [ ] Is there proper logging for critical failures?

## Testing
- [ ] Are there unit or integration tests for the new code?
- [ ] Do the tests cover edge cases and error paths?
- [ ] Do all existing tests still pass?

## Documentation
- [ ] Are public APIs or complex logic documented with comments?
- [ ] Is the `README` or other documentation updated if needed?
