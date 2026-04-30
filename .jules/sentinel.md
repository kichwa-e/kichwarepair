## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-25 - Tailwind CDN and script-src CSP
**Vulnerability:** Weak Content Security Policy (`script-src 'unsafe-inline'`) allowing potential Cross-Site Scripting (XSS).
**Learning:** By externalizing inline scripts (`tailwind-config.js` and other app logic) when using the Tailwind Play CDN, `unsafe-inline` can be safely removed from `script-src`, significantly hardening the application against XSS attacks.
**Prevention:** Always externalize inline scripts and configurations to separate `.js` files. When using Tailwind Play CDN, load the externalized config script immediately after the CDN script.
