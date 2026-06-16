## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-05-14 - Externalizing inline scripts for strict CSP
**Vulnerability:** Inline scripts required 'unsafe-inline' in script-src CSP directive, which increases XSS risk.
**Learning:** Tailwind config and application logic can be easily extracted to external .js files, allowing the removal of 'unsafe-inline' from script-src.
**Prevention:** Always use external script files instead of inline <script> tags to maintain a strict CSP.
