import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_form_security_attributes(page: Page):
    file_path = pathlib.Path('kichwa_repair_with_blue_green_logo.html').resolve().as_uri()

    # Intercept and block unnecessary non-file requests to speed up testing
    # but allow tailwind if used, although we just check DOM attributes here.
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(file_path)

    # Find the form elements
    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_textarea = page.locator('textarea[name="issue"]')

    # Wait for the elements to be present
    expect(name_input).to_be_visible()
    expect(phone_input).to_be_visible()
    expect(issue_textarea).to_be_visible()

    # Check maxlength attributes
    assert name_input.get_attribute("maxlength") == "100", "Name input should have maxlength=100"
    assert phone_input.get_attribute("maxlength") == "20", "Phone input should have maxlength=20"
    assert issue_textarea.get_attribute("maxlength") == "1000", "Issue textarea should have maxlength=1000"

    # Check pattern attribute for phone using evaluate to bypass python encoding issues
    phone_pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert phone_pattern == r"^[\d\s\+\-\(\)]+$", f"Phone input pattern incorrect. Got: {phone_pattern}"

    # Verify the security comment is present
    page_content = page.content()
    assert "<!-- SECURITY: Added input length limits (maxlength) and validation patterns to prevent DoS via large payloads and enforce expected data formats -->" in page_content, "Security comment should be present"
