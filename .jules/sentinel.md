## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Form Input Validation
**Vulnerability:** Missing input limits (maxlength) and validation logic on user-facing forms, leading to potential DoS (via excessively large inputs) or unexpected data formats.
**Learning:** For name fields, strict regex patterns block non-Latin characters. It is safer to rely on `maxlength` (e.g. 100) instead of restrictive pattern matches. Phone numbers should allow spaces, plus signs, hyphens, and parentheses.
**Prevention:** Always include reasonable `maxlength` attributes for all text and textarea fields, and use carefully constructed regex patterns for numeric/phone inputs that allow standard formatting characters.
