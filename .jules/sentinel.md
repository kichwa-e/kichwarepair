## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2025-02-14 - Client-side Validation on Netlify Forms
**Vulnerability:** Missing input length and pattern constraints on user forms (name, phone, issue).
**Learning:** Because the project utilizes Netlify Forms (`data-netlify="true"`) where backend validation is abstracted, client-side input validation (e.g., `maxlength`, `pattern`) is a critical initial layer of defense against oversized payloads and malformed data.
**Prevention:** Always implement robust HTML5 validation attributes (`maxlength`, `pattern`) on forms that bypass custom backend code and integrate directly with serverless platforms.
