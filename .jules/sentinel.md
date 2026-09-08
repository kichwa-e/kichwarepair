## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-09-08 - Add input validation on user form
**Vulnerability:** Missing client-side input length and pattern validation on the 'quote' form.
**Learning:** Projects using Netlify Forms (data-netlify="true") abstract backend validation, making client-side constraints the primary defense against malformed data and oversized payloads.
**Prevention:** Always include reasonable `maxlength` and appropriate `pattern` limits on all text inputs and textareas in serverless form setups.
