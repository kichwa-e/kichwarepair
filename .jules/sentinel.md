## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-10-05 - Add Input Validation on Client Forms
**Vulnerability:** Found an HTML form in `kichwa_repair_with_blue_green_logo.html` that sends data via Netlify Forms without explicit client-side length or format validation.
**Learning:** Because Netlify Forms process backend submissions natively, relying solely on their infrastructure without client-side limits opens up risk for malformed data and minor application layer DoS via oversized payloads.
**Prevention:** Always implement basic HTML5 attributes (`maxlength`, `pattern`, `required`) as an initial defense-in-depth layer on all publicly accessible forms, even when using third-party form handlers.
