import pytest
from playwright.sync_api import Page
import pathlib

def test_security_input_limits(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path)

    # Check maxlengths
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute('maxlength') == '100'

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute('maxlength') == '50'
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_input = page.locator('textarea[name="issue"]')
    assert issue_input.get_attribute('maxlength') == '1000'
