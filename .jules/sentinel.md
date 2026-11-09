## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-11-09 - Meta Tag CSP Limitations
**Vulnerability:** Ineffective clickjacking protection.
**Learning:** The `frame-ancestors` Content Security Policy directive is not supported and is ignored by browsers when delivered via a `<meta>` tag. It must be delivered via an HTTP response header to be effective.
**Prevention:** Do not include `frame-ancestors` when configuring CSP via `<meta>` tags. Focus on directives like `default-src`, `object-src`, and `form-action` which are supported.
