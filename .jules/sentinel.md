## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2026-05-24 - Tailwind CDN SRI Unsupported
**Vulnerability:** Attempted to add Subresource Integrity (SRI) to `cdn.tailwindcss.com`.
**Learning:** `cdn.tailwindcss.com` does not serve files with the `Access-Control-Allow-Origin` header. Adding `crossorigin="anonymous"` (required for SRI) causes the browser to block the script due to CORS policy, completely breaking the application's CSS.
**Prevention:** Pin the Tailwind CDN version (`<script src="https://cdn.tailwindcss.com/3.4.5"></script>`) without `integrity` and `crossorigin` attributes.
