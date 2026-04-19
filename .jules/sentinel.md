## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-02-24 - Form Input Validation
**Vulnerability:** Missing client-side input validation on Netlify forms (potential DoS risk and junk submissions).
**Learning:** The application leverages Netlify forms (`data-netlify="true"`), meaning backend processing is handled automatically. Therefore, robust client-side HTML input validation (`maxlength`, `pattern`, `type="tel"`) serves as the primary defense mechanism against junk submissions and excessive payload sizes.
**Prevention:** Always enforce client-side HTML limits on form fields using attributes like `maxlength`, `pattern`, `type`, and `required` to prevent excessive payloads and ensure basic validation before submission.
