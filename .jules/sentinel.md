## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-03-16 - Netlify Forms Validation
**Vulnerability:** Missing input validation and length limits on Netlify form inputs leading to potential DoS via large payloads or junk data injection.
**Learning:** Serverless forms, such as those provided by Netlify (`data-netlify="true"`), often lack custom backend validation hooks by default. Therefore, robust client-side HTML validation (e.g., `maxlength`, `pattern`, `type`, `required`) becomes the critical primary defense layer against invalid data and excessively large payloads.
**Prevention:** Always implement strict HTML validation attributes (`maxlength`, `type`, `pattern`, `required`) on all client-side forms, especially those relying on serverless form processors, to ensure data integrity and mitigate DoS risks.
