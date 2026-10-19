## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-02-25 - Netlify Form Client-Side Validation
**Vulnerability:** Netlify forms abstract backend validation, meaning without client-side HTML attributes (`pattern`, `maxlength`), the form is susceptible to malformed data and oversized payloads (DoS risk).
**Learning:** Because there's no custom backend code to enforce validation on Netlify forms (`data-netlify="true"`), the frontend HTML acts as the primary defense layer.
**Prevention:** Always enforce strict `pattern`, `maxlength`, and `type` attributes on all fields submitted via Netlify forms.
