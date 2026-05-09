## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-04-13 - [DoS Risk via Netlify Forms]
**Vulnerability:** [Missing input constraints on a Netlify form allowed potential Denial of Service via large payloads.]
**Learning:** [Netlify forms process data automatically on the backend, making client-side constraints the primary defense mechanism against junk and large submissions.]
**Prevention:** [Always enforce required, maxlength, type, and regex patterns on client-facing inputs for Netlify forms.]
