import pytest
from playwright.sync_api import Page
import pathlib

def test_form_security_validation(page: Page):
    uri = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()

    # Route to allow file and tailwind, abort others
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(uri)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_input = page.locator('textarea[name="issue"]')

    assert name_input.get_attribute('maxlength') == '100'
    assert phone_input.get_attribute('maxlength') == '50'
    assert phone_input.get_attribute('type') == 'tel'
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
    assert issue_input.get_attribute('maxlength') == '1000'
