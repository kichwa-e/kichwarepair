## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-04-24 - Strict CSP for Tailwind CDN
**Vulnerability:** XSS risk from 'unsafe-inline' in script-src CSP directive.
**Learning:** While Tailwind CDN needs 'unsafe-inline' in style-src, the script-src can be strict if configuration and app logic are moved to external files.
**Prevention:** Always externalize inline JavaScript, even simple configuration blocks or UI toggles, to enable strict script-src CSP rules.
