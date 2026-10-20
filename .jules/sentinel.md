## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-12-04 - Unvalidated Netlify Form Payloads
**Vulnerability:** Missing client-side input validation on Netlify forms (`data-netlify="true"`), allowing potentially massive or malformed data submissions.
**Learning:** Because Netlify abstracts backend validation, the first line of defense must be robust client-side `maxlength` and regex `pattern` attributes to prevent oversized payload abuse or junk data ingestion.
**Prevention:** Always enforce strict `maxlength` bounds and structural `pattern` validation (e.g., `^[\p{L}\s\-']+$` for names) on static forms before deploying to serverless platforms.
