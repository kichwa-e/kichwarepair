## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Externalize Scripts for CSP
**Vulnerability:** Use of `'unsafe-inline'` in `script-src` CSP directive due to inline scripts.
**Learning:** Inline application logic (e.g., mobile menu toggles, dynamic footer year) and Tailwind configuration can be externalized into `app.js` and `tailwind-config.js` to maintain a strict Content Security Policy without relying on `unsafe-inline` in `script-src`.
**Prevention:** Always externalize scripts and configurations into separate `.js` files when using a CSP. The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with a strict `script-src` if its configuration is loaded from an external file.
