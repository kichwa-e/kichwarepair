import pytest
from playwright.sync_api import Page
import pathlib

def test_form_security_attributes(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / "kichwa_repair_with_blue_green_logo.html"
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path.resolve().as_uri())

    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute('maxlength') == '100'

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute('maxlength') == '20'
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute('maxlength') == '1000'
