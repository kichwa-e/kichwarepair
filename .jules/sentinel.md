## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-06-25 - Missing Input Validation on Netlify Form
**Vulnerability:** The quote form in `kichwa_repair_with_blue_green_logo.html` lacked client-side validation (`maxlength` and `pattern` attributes).
**Learning:** Netlify Forms abstract backend validation. Client-side input validation is a critical initial layer of defense against oversized payloads and malformed data.
**Prevention:** Ensure all form fields have appropriate `maxlength` and `pattern` validation attributes implemented on the client side.
