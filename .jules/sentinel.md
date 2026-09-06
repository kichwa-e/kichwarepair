## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-02-24 - Form Input Validation
**Vulnerability:** Missing client-side input validation on Netlify forms allowed oversized payloads and malformed data.
**Learning:** Netlify forms abstract backend validation. Client-side attributes like `maxlength` and `pattern` are critical for defense in depth. Name fields should avoid strict regex (to support global names) and rely on `maxlength`, while phone fields can use flexible patterns (e.g., `^[\d\s\+\-\(\)]+$`).
**Prevention:** Always add `maxlength` and appropriate `pattern` validation to user-facing form inputs.
