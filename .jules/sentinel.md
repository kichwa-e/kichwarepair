## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-10-26 - Static Form Validation
**Vulnerability:** Missing client-side input validation (`maxlength`, `pattern`) on user-facing forms.
**Learning:** In static sites utilizing services like Netlify Forms (`data-netlify="true"`) where backend validation is abstracted, client-side constraints are a critical initial layer of defense-in-depth against oversized payloads and malformed data.
**Prevention:** Always enforce `maxlength` and regex `pattern` attributes on all form inputs, especially when direct backend control is limited.
