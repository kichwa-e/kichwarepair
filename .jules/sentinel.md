## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2025-02-13 - Add input validation on user form
**Vulnerability:** Missing client-side input validation on Netlify forms allows potentially oversized or malformed data submissions.
**Learning:** Since Netlify Forms abstracts backend validation, client-side constraints (maxlength, pattern) serve as a crucial first line of defense.
**Prevention:** Always add HTML5 validation attributes (`maxlength`, `pattern`, `type`) to form fields relying on third-party form processors.
