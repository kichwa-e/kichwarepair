## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-10-04 - Missing Input Validation on Netlify Forms
**Vulnerability:** Abstracted backend forms (data-netlify="true") lacked client-side input validation (e.g., maxlength, pattern) for name, phone, and text fields, creating a risk of oversized payloads and malformed data.
**Learning:** Because backend validation is handled externally by Netlify, client-side HTML5 validation is a critical initial layer of defense that cannot be overlooked.
**Prevention:** Always implement standard HTML5 input validation attributes (maxlength, pattern, required) on all form elements when using static site form providers.
