## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Remove unsafe-inline from script-src
**Vulnerability:** Weak Content Security Policy (CSP) allowing inline scripts (XSS risk).
**Learning:** Application logic and Tailwind configuration can be externalized to remove the `unsafe-inline` requirement for `script-src`, hardening the CSP. The Tailwind Play CDN itself only requires `unsafe-inline` for `style-src` but not `script-src` if config is loaded via external script.
**Prevention:** Always externalize scripts (`app.js`, `tailwind-config.js`) to allow for a stricter `script-src` CSP without `unsafe-inline`.
