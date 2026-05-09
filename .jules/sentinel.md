## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-04-02 - Netlify Form Input Validation
**Vulnerability:** Missing client-side input validation on Netlify forms, allowing potentially massive payloads and invalid data to be submitted.
**Learning:** Because the backend is abstracted away by Netlify Forms (`data-netlify="true"`), we cannot implement custom server-side input validation logic directly. Thus, robust client-side HTML validation (e.g., `maxlength`, `pattern`, `type="tel"`) becomes our primary defense mechanism against junk submissions and DoS via excessive payload sizes.
**Prevention:** Always enforce strict HTML5 validation attributes (`required`, `maxlength`, and correct input types/patterns) on all fields within forms handled by third-party backend services like Netlify.
