## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Client-side validation for Netlify Forms
**Vulnerability:** Missing input constraints (maxlength, pattern) on Netlify-processed forms allowed potentially oversized payloads or malformed data submission.
**Learning:** Because Netlify Forms handles backend processing opaquely, client-side validation is the critical first layer of defense. Without HTML5 validation constraints, users could submit arbitrary length strings or non-numeric phone numbers.
**Prevention:** Always add appropriate `maxlength` and `pattern` attributes to form fields, particularly when relying on third-party form processors where backend validation is abstracted.
