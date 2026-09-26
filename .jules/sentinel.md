## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-09-26 - Client-Side Validation for Abstracted Backends
**Vulnerability:** Missing input validation (maxlength, pattern) on user-facing forms (Netlify Forms).
**Learning:** Because backend validation is abstracted by Netlify Forms (`data-netlify="true"`), client-side constraints are the critical first layer of defense against oversized payloads and malformed data.
**Prevention:** Always implement robust HTML5 validation (`maxlength`, `pattern`) on forms that rely on third-party submission endpoints without customizable backend sanitization.
