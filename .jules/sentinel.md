## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.

## 2024-05-18 - Missing Input Validation
**Vulnerability:** Found missing input validation on form inputs in `kichwa_repair_with_blue_green_logo.html`
**Learning:** Netlify forms abstract backend processing, requiring strict client-side validation as the primary defense against malformed or excessive input. Double-escaping regex character classes in HTML pattern attributes (like `pattern="^[\\p{L}]+$"`) causes them to fail parsing in browsers. Ensure a single backslash is rendered in the final HTML (like `pattern="^[\p{L}]+$"`).
**Prevention:** Always add `maxlength`, `pattern`, and proper types to HTML inputs. Use four backslashes when writing `sed` commands in JSON tool arguments to ensure exactly one backslash is output to the HTML file.
