## 2024-05-24 - Input Validation Missing on Form
**Vulnerability:** Missing input validation (length limits and format restrictions) on the Netlify form fields in `kichwa_repair_with_blue_green_logo.html`.
**Learning:** Forms handled by third-party services (like Netlify Forms via `data-netlify="true"`) abstract backend processing, making client-side input validation a crucial first layer of defense against oversized payloads and malformed data.
**Prevention:** Always implement HTML5 validation attributes (`maxlength`, `pattern`) as an initial defense, even when backend validation is handled by a managed service.
