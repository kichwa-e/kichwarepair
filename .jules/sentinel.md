## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-02-24 - Tabnabbing Risk in External Links
**Vulnerability:** External utility links (like WhatsApp URLs `https://wa.me/...`) were opening in the same tab, or without `target="_blank" rel="noopener noreferrer"`.
**Learning:** Using `target="_blank"` without `rel="noopener noreferrer"` allows the newly opened tab to potentially hijack the original tab via `window.opener`. While modern browsers mitigate this by defaulting to `noopener`, explicitly defining both attributes remains a universally recommended security best practice, especially for external domains. Additionally, utility links should open in new tabs to prevent navigating users away from the core application.
**Prevention:** Always append `target="_blank" rel="noopener noreferrer"` to any external link pointing outside the current domain, especially utility links like WhatsApp or social media.
