## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-05-24 - Netlify Forms DoS Protection
**Vulnerability:** Missing strict input validation on Netlify forms leading to potential DoS via large payloads and junk submissions.
**Learning:** Because Netlify processes form submissions automatically without backend validation logic, client-side HTML input validation serves as the primary defense mechanism.
**Prevention:** Always enforce maxlength, appropriate type attributes (e.g., tel), and strict regex pattern attributes on all <input> and <textarea> elements within data-netlify="true" forms.
