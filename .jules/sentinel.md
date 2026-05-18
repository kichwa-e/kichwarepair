## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-10-24 - Strict CSP with Tailwind CDN
**Vulnerability:** XSS vulnerability due to 'unsafe-inline' in script-src.
**Learning:** The Tailwind Play CDN configuration can be externalized to a separate JS file. This eliminates the need for 'unsafe-inline' in the `script-src` directive, allowing for a stricter CSP baseline than previously documented.
**Prevention:** Always externalize application logic and Tailwind configurations. Ensure the CSP baseline is: `default-src 'self'; script-src 'self' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
