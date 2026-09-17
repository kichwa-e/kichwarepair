## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-10-25 - Sentinel: Add input validation on user form
**Vulnerability:** Missing input validation (`maxlength`, `pattern`) on the contact form inputs in `kichwa_repair_with_blue_green_logo.html`.
**Learning:** Because the backend uses Netlify Forms which abstracts processing, client-side input validation is the critical first layer of defense against oversized payloads and malformed data.
**Prevention:** Always add appropriate `maxlength` and `pattern` constraints to form inputs, especially when backend processing is handled externally.
