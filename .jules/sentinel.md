## 2024-09-04 - Unvalidated Netlify Form Inputs
**Vulnerability:** The Netlify-powered contact form lacked client-side input validation, allowing potentially unbounded or malformed data submissions.
**Learning:** Because backend validation is handled externally by Netlify, the static site relies entirely on client-side constraints as its first line of defense to enforce data integrity and prevent oversized payloads.
**Prevention:** Always implement HTML5 validation attributes (`maxlength`, `pattern`, `type`) on public-facing form fields, even when the backend is managed by a third-party service.
