## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Tabnabbing Vulnerability on External Links
**Vulnerability:** External WhatsApp links (`https://wa.me/...`) were opening without `target="_blank"` and `rel="noopener noreferrer"`. If they were to be changed to open in a new tab without the `rel` attribute, they would be vulnerable to reverse tabnabbing attacks.
**Learning:** Even if an external link opens in the same tab, it is good practice to enforce `target="_blank" rel="noopener noreferrer"` for external call-to-actions to prevent tabnabbing if the target behavior is ever updated, and to ensure users do not lose their session on the main application.
**Prevention:** Always include `target="_blank" rel="noopener noreferrer"` on all external links, especially for external communication platforms like WhatsApp.
