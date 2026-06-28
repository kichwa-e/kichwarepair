import pytest
from playwright.sync_api import Page
import pathlib

def test_form_security_attributes(page: Page):
    # Resolve the file path to a local URI
    file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'

    # Route configuration to mock external requests but allow file and tailwindcss requests
    page.route('**/*', lambda route: route.continue_() if route.request.url.startswith('file://') or route.request.url.startswith('https://cdn.tailwindcss.com') else route.abort())

    page.goto(file_path.resolve().as_uri())

    # Verify Name field attributes
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"
    assert name_input.evaluate('el => el.getAttribute("pattern")') is None

    # Verify Phone field attributes
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    phone_pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert phone_pattern == r"^[\d\s\+\-\(\)]+$"

    # Verify Issue textarea attributes
    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute("maxlength") == "500"
