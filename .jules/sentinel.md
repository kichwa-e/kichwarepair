## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-05-16 - Static HTML Strict CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS in purely static pages.
**Learning:** For completely static pages like `kichwa-connect.html` that have no JavaScript logic, the safest baseline CSP restricts `script-src` to `'none'`. This prevents XSS attacks effectively at the structural level.
**Prevention:** Use the baseline CSP `default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'self';` for static pages without scripts.
