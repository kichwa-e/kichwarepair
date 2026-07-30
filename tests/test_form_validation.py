import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_form_validation(page: Page):
    html_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'
    uri = html_path.resolve().as_uri()

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(uri)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_textarea = page.locator('textarea[name="issue"]')

    expect(name_input).to_have_attribute("maxlength", "100")
    expect(phone_input).to_have_attribute("maxlength", "20")
    expect(issue_textarea).to_have_attribute("maxlength", "1000")

    phone_pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert phone_pattern == r"^[\d\s\+\-\(\)]+$"
