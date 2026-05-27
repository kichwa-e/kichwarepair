## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-05-27 - Tailwind CDN Strict CSP
**Vulnerability:** Overly permissive CSP ('unsafe-inline' in script-src) allowing XSS.
**Learning:** Contrary to previous assumptions, Tailwind Play CDN does NOT require 'unsafe-inline' in script-src. The configuration and app logic can be safely externalized to separate files (e.g., tailwind-config.js, app.js) loaded via standard script tags without breaking functionality.
**Prevention:** Always externalize inline scripts and use the stricter CSP baseline for script-src: `script-src 'self' https://cdn.tailwindcss.com;` to prevent XSS.
