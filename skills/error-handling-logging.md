---
name: error-handling-logging
description: Guidelines for robust error management and informative logging. Use to build resilient systems that are easy to debug and monitor.
---

# Error Handling and Logging

## Error Handling Principles
- **Fail Fast**: Detect and report errors as close to the source as possible.
- **Be Specific**: Use custom exception types where appropriate.
- **Don't Swallow Errors**: Never use an empty `catch` block. At a minimum, log the error.
- **Graceful Degradation**: If a non-critical feature fails, the application should continue to work.
- **Clean Up**: Use `finally` or `try-with-resources` to ensure files, sockets, and database connections are closed.

## Logging Principles
- **Log Level Awareness**:
    - **ERROR**: Critical failures that need immediate attention.
    - **WARN**: Unexpected behavior that the system can recover from.
    - **INFO**: Important business milestones or system state changes.
    - **DEBUG**: Verbose information for developers during troubleshooting.
- **Structured Logging**: Use JSON format for logs to make them searchable by machines.
- **Context is King**: Always include relevant IDs (User ID, Request ID) in your log messages.
- **No PII**: NEVER log personally identifiable information (passwords, emails, phone numbers).

## Workflow
1. **Define Strategy**: Determine which layers of the app handle errors vs. bubble them up.
2. **Implement Catchers**: Wrap risky operations (I/O, API calls) in try-catch blocks.
3. **Log Exceptions**: Log the FULL stack trace for ERRORS, but just the message for WARNs.
4. **Monitor**: Use tools (Sentry, ELK, Datadog) to alert on ERROR level logs.
