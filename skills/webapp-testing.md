---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

## Methodology
Use Playwright to automate and verify local web applications.

## Decision Tree
- **Static HTML**: Read file directly, write simple Playwright script.
- **Dynamic Webapp**:
    1. Start server (capture port).
    2. Navigate and wait for `networkidle`.
    3. Take screenshot and inspect DOM to find selectors.
    4. Execute test actions.

## Playwright Basics (Python)
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')
    # Actions
    page.click('button#submit')
    # Verification
    assert page.is_visible('.success-message')
    browser.close()
```

## Best Practices
- **Wait for JS**: Always wait for `networkidle` or specific selectors before interacting.
- **Screenshots**: Use `page.screenshot(path='debug.png')` to visually verify state during testing.
- **Selectors**: Prefer robust selectors like `role=button`, `text="Submit"`, or IDs.
- **Capture Logs**: Monitor `page.on("console", lambda msg: print(msg.text))` for errors.
- **Clean Up**: Always close the browser to release resources.
