## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-05-18 - Client-Side Validation on Serverless Forms
**Vulnerability:** Missing client-side input constraints (maxlength, pattern) on Netlify Forms.
**Learning:** When using serverless form providers like Netlify (`data-netlify="true"`), backend validation is abstracted away. Client-side HTML5 validation becomes the critical first line of defense against oversized payloads and malformed data.
**Prevention:** Always include `maxlength` attributes for text inputs and `pattern` regex for structured fields (like phone numbers) on all frontend forms, especially those submitted directly to third-party providers.
