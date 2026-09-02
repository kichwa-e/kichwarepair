## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-09-02 - Add client-side input validation
**Vulnerability:** The quote form in `kichwa_repair_with_blue_green_logo.html` was missing client-side input validation, making it susceptible to excessive input length attacks and format abuse.
**Learning:** Always include `maxlength` limits and appropriate regex patterns for specific fields like phone numbers to protect against basic DoS and enforce expected data formats without blocking valid international characters.
**Prevention:** Integrate `maxlength` and `pattern` attributes into all new HTML forms.
