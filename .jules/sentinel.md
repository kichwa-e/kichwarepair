## 2026-02-24 - Tailwind CDN CSP
**Vulnerability:** Missing Content Security Policy (CSP) allowing potential XSS.
**Learning:** The Tailwind Play CDN (`https://cdn.tailwindcss.com`) works correctly with `script-src` and `style-src` directives, but requires `unsafe-inline` for both due to inline configuration and style injection. Crucially, it does NOT require `unsafe-eval` for basic usage in this project, allowing for a stricter policy than initially expected.
**Prevention:** Use the following CSP baseline for Tailwind CDN projects: `default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline';`.
## 2026-02-24 - HTML5 Pattern Regex Escaping
**Vulnerability:** Not a direct vulnerability, but a regression risk when applying client-side input validation enhancements via regex patterns.
**Learning:** When defining regular expressions in HTML `pattern` attributes, the backslash (`\`) is not an escape character for the string itself. To use regex character classes (like `\d` or `\p{L}`), ensure the final HTML contains exactly one backslash (e.g., `pattern="^[\d]+$"`). If double-escaped (e.g., `\\d`), the HTML parser treats it as a literal backslash, causing the pattern validation to fail or block valid input.
**Prevention:** Always verify the final rendered HTML output. When using automated tools (like `sed`) to inject patterns, account for the shell/JSON escape sequences required to output exactly *one* backslash in the final file.
