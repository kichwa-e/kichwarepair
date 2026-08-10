import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_form_security_validation(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve()
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path.as_uri())

    # Wait for DOM content to ensure tailwind processes
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "20")
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
