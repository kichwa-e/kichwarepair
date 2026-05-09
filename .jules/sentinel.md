## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-05-24 - Missing Input Validation on Netlify Forms
**Vulnerability:** Missing client-side input validation (`maxlength`, `pattern`, `type`) on Netlify forms allows potential Denial of Service (DoS) attacks via excessively large payloads or junk submissions.
**Learning:** Netlify handles backend processing automatically for forms with `data-netlify="true"`. Without explicit server-side validation logic available to edit, robust client-side HTML input validation must serve as the primary defense mechanism against abuse.
**Prevention:** Always enforce strict constraints (`maxlength`, `required`, correct `type`, and regex `pattern`) on all Netlify form inputs.
