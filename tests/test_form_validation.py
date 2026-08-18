import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_form_validation(page: Page):
    file_uri = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_uri, wait_until="domcontentloaded")
    page.wait_for_timeout(1000)

    # Check maxlengths
    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_input = page.locator('textarea[name="issue"]')

    expect(name_input).to_have_attribute("maxlength", "100")
    expect(phone_input).to_have_attribute("maxlength", "20")
    expect(issue_input).to_have_attribute("maxlength", "1000")

    # Check pattern
    phone_pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert phone_pattern == r"^[\d\s\+\-\(\)]+$"
