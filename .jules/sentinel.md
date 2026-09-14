## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-05-18 - Client-Side Validation on Forms
**Vulnerability:** The Netlify form lacked client-side input validation and length limits on input and textarea fields.
**Learning:** Netlify abstractions handle backend processing seamlessly, but they inherently omit client-side defense. Over-reliance on abstracted services often leads to neglecting first-layer protections like length bounding (`maxlength`) and format bounding (`pattern`).
**Prevention:** Always combine abstracted backend processors with robust client-side bounds as standard practice to reject oversized/malformed data as early as possible.
