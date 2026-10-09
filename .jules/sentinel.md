## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-02-24 - Netlify Forms Client-Side Validation
**Vulnerability:** Missing input validation on Netlify forms (`name="quote"`).
**Learning:** Netlify Forms (`data-netlify="true"`) abstract backend processing, making client-side input validation (e.g., `maxlength`, `pattern`) a critical initial layer of defense against oversized payloads and malformed data.
**Prevention:** Always implement `maxlength` and appropriate `pattern` attributes for Netlify form inputs.
