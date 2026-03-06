import re

with open('kichwa_repair_with_blue_green_logo.html', 'r') as f:
    content = f.read()

assert 'maxlength="100" name="name"' in content, "Name validation failed"
assert 'maxlength="20" name="phone" pattern="[0-9+ \-]{10,20}"' in content and 'type="tel"' in content, "Phone validation failed"
assert 'maxlength="500" name="issue"' in content and 'required=""' in content, "Issue validation failed"
assert '<!-- 🛡️ Sentinel: Added missing input validation and length limits to form fields to prevent DoS via large payloads and ensure data integrity. -->' in content, "Sentinel comment missing"

print("All validations passed!")