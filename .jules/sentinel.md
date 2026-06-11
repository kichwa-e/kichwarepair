## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Reverse Tabnabbing Vulnerability
**Vulnerability:** External WhatsApp links (`https://wa.me/...`) lacked `target="_blank"` and `rel="noopener noreferrer"`.
**Learning:** External links, particularly to messaging services, should isolate the new tab's execution context to prevent reverse tabnabbing and improve UX by not navigating away from the main site.
**Prevention:** Always add `target="_blank" rel="noopener noreferrer"` to external links.
