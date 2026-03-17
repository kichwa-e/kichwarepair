## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-03-17 - Netlify Form DoS via Unrestricted Inputs
**Vulnerability:** Missing length and format constraints on Netlify form inputs (`<input>` and `<textarea>`) allowed potential Denial of Service (DoS) and data pollution via extremely large or malformed payloads.
**Learning:** Because backend processing is handled automatically by Netlify (`data-netlify="true"`), there is no custom server-side validation logic available to reject junk or excessively large submissions before they consume quota.
**Prevention:** Implement strict client-side validation as the primary defense: mandate `required`, enforce reasonable `maxlength` limits (e.g., Name: 100, Phone: 20, Issue: 500), and use appropriate input types (`type="tel"`) with regex `pattern` validation for specific formats.
