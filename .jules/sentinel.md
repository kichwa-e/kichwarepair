## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-25 - Strict CSP for Tailwind
**Vulnerability:** XSS risk due to `unsafe-inline` in `script-src` directive of CSP.
**Learning:** While the Tailwind Play CDN injects inline styles requiring `unsafe-inline` in `style-src`, it does not require `unsafe-inline` in `script-src` if the `tailwind.config` and other application logic are externalized into separate JavaScript files.
**Prevention:** Always externalize scripts and use a strict `script-src` baseline: `script-src 'self' https://cdn.tailwindcss.com;`.
