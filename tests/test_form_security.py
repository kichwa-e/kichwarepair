import pathlib
import pytest
from playwright.sync_api import Page

def test_form_security_attributes(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()
    page.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file://") or r.request.url.startswith("https://cdn.tailwindcss.com") else r.abort())
    page.goto(file_path)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)

    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute("maxlength") == "1000"
