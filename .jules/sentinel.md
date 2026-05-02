## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Strict CSP with Tailwind CDN
**Vulnerability:** Weak Content Security Policy using 'unsafe-inline' for script-src.
**Learning:** Even when using Tailwind CDN, inline scripts for configuration or app logic can be externalized into separate files (e.g., tailwind-config.js, app.js). This allows the removal of 'unsafe-inline' from the script-src directive, significantly reducing XSS risks without breaking functionality.
**Prevention:** Always externalize inline scripts and configuration when using Tailwind CDN, and use a strict CSP: `default-src 'self'; script-src 'self' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
