## 2026-02-23 - Verifying CSP on Static Sites
**Vulnerability:** CSP changes can silently break functionality if resources are blocked.
**Learning:** Playwright's console listener is essential for detecting CSP violations on static sites where server logs are unavailable.
**Prevention:** Use a local server + Playwright script to intercept console errors before deploying CSP changes.
