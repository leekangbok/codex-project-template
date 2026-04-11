---
name: security-audit
description: Checklist and methodology for auditing code for security vulnerabilities. Use when reviewing code for safety or conducting a security-focused sweep.
---

# Security Audit Checklist

## Injection Attacks
- [ ] **SQL Injection**: Are all database queries using prepared statements or parameterized queries?
- [ ] **Command Injection**: Is user input used in shell commands? If so, is it properly escaped?
- [ ] **NoSQL Injection**: Is user input sanitized before being used in NoSQL queries?

## Cross-Site Scripting (XSS)
- [ ] Is all user-generated content escaped before being rendered in the browser?
- [ ] Are `Content-Security-Policy` headers in place?
- [ ] Are `HttpOnly` and `Secure` flags set on cookies?

## Authentication & Authorization
- [ ] are passwords hashed with a strong algorithm (e.g., Argon2, bcrypt)?
- [ ] Is there a rate-limiting mechanism for login attempts?
- [ ] Are permissions checked for EVERY sensitive action or data access?
- [ ] Are sensitive tokens (JWT, API keys) stored safely?

## Data Protection
- [ ] Is sensitive data encrypted at rest and in transit (HTTPS)?
- [ ] Are secrets (API keys, DB passwords) removed from source code and managed via environment variables or secret managers?
- [ ] Does the application log sensitive information (PII, passwords, credit card numbers)?

## Dependencies
- [ ] Are there any known vulnerabilities in third-party packages? (Run `npm audit`, `pip-audit`, etc.)
- [ ] Are dependencies pinned to specific versions?

## Error Handling
- [ ] Do error messages reveal system information (stack traces, server versions, database schema)?
- [ ] Is there a generic "Something went wrong" message for end users?
