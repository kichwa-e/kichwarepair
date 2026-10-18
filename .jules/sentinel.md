## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2025-05-18 - Add input validation to Netlify forms
**Vulnerability:** Forms using `data-netlify="true"` handle submissions automatically, bypassing custom backend validation. This leaves the system vulnerable to oversized payloads and malformed data if client-side validation is missing.
**Learning:** Netlify's built-in form handling abstracts away the backend, making client-side input validation (e.g., `maxlength`, `pattern`) the critical primary layer of defense against abuse.
**Prevention:** Always enforce strict `maxlength` limits and appropriate `pattern` constraints on HTML input elements when relying on third-party form providers like Netlify.
