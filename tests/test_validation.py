import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_form_validation(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / "kichwa_repair_with_blue_green_logo.html"
    file_uri = file_path.resolve().as_uri()

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_uri)
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_input = page.locator('textarea[name="issue"]')

    assert name_input.get_attribute("maxlength") == "100"
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
    assert issue_input.get_attribute("maxlength") == "1000"
