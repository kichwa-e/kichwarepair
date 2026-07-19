import pytest
from playwright.sync_api import Page
import pathlib

def test_form_validation(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / "kichwa_repair_with_blue_green_logo.html"
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path.resolve().as_uri())

    # Wait for the form to be loaded
    page.wait_for_selector('form[name="quote"]')

    # Assert name field constraints
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    # Assert phone field constraints
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    # Assert issue field constraints
    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute("maxlength") == "1000"
