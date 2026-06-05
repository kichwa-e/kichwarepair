## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-06-05 - Reverse Tabnabbing Prevention on External App Links
**Vulnerability:** External WhatsApp (`wa.me`) links were missing `rel="noopener noreferrer"`.
**Learning:** While `target="_blank"` improves UX for messaging links so users don't lose the main site, omitting `rel="noopener noreferrer"` exposes the site to reverse tabnabbing where the opened third-party site could potentially manipulate the `window.opener`. Furthermore, `noreferrer` provides a privacy enhancement by omitting the `Referer` header to the third-party chat app.
**Prevention:** Always append `rel="noopener noreferrer"` to any external link (especially those pointing to messaging apps or unknown domains) that uses `target="_blank"`.
