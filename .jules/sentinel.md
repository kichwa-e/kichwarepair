## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Strict CSP with Tailwind CDN
**Vulnerability:** Inline scripts required `'unsafe-inline'` in `script-src`, opening the door to XSS.
**Learning:** The Tailwind configuration object and application logic can be safely externalized to separate `.js` files and loaded after the CDN script, removing the need for `'unsafe-inline'` in `script-src` while preserving dynamic styling.
**Prevention:** Always externalize Tailwind configuration and application logic scripts when using the Play CDN to enforce a stricter CSP baseline: `default-src 'self'; script-src 'self' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
