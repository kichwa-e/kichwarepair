## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-25 - Strict CSP with Tailwind CDN
**Vulnerability:** Inline scripts required 'unsafe-inline' in script-src, enabling potential XSS attacks.
**Learning:** 'unsafe-inline' can be completely removed from script-src when using the Tailwind CDN by moving all application logic (e.g., app.js) and the Tailwind configuration object (tailwind.config) into external `.js` files. The CDN script itself still functions perfectly.
**Prevention:** Always externalize inline JavaScript and configuration objects into separate files to allow for a strict Content Security Policy (`script-src 'self' https://cdn.tailwindcss.com;`) without needing 'unsafe-inline'.
