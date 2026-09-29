## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2025-02-14 - Add input validation on user form
**Vulnerability:** Found forms lacking input validation (`maxlength`, `pattern`) which can lead to oversized payloads and malformed data.
**Learning:** Netlify Forms (`data-netlify="true"`) abstract backend validation, making client-side input validation a critical initial layer of defense against malicious input.
**Prevention:** Always implement `maxlength` and `pattern` attributes for HTML forms, even when backend validation is handled by third parties.
