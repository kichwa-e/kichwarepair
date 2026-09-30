## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2024-09-30 - Client-Side Validation Missing on Netlify Forms
**Vulnerability:** Input fields (`name`, `phone`, `issue`) in the Netlify form (`data-netlify="true"`) lacked explicit client-side validation (`maxlength`, `pattern`), creating an unnecessary risk of oversized payloads and malformed data submission.
**Learning:** Because Netlify abstracts backend processing, the frontend `<form>` validation is the primary line of defense against DoS via huge payloads and junk submissions.
**Prevention:** Always include `maxlength`, `pattern`, and `type` constraints on form inputs, especially when using serverless/third-party form handlers.
