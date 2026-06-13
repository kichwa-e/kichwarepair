import pytest
import pathlib
from playwright.sync_api import sync_playwright

def test_form_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        file_path = str((pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html').resolve())
        page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
        page.goto(f"file://{file_path}", wait_until="domcontentloaded")

        name_input = page.locator('input[name="name"]')
        # use raw strings and evaluate instead of straight Python equality to bypass unicode conversion differences
        assert name_input.evaluate('el => el.getAttribute("pattern")') == r"^[a-zA-Z\xC0-\xFF\s\-'\.]+$"
        assert name_input.get_attribute("maxlength") == "100"

        phone_input = page.locator('input[name="phone"]')
        assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
        assert phone_input.get_attribute("maxlength") == "20"

        issue_input = page.locator('textarea[name="issue"]')
        assert issue_input.get_attribute("maxlength") == "500"

        browser.close()
