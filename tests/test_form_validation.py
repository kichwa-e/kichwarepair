import pytest
from playwright.sync_api import Page, expect

def test_form_validation(page: Page):
    import os
    file_uri = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(file_uri)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_input = page.locator('textarea[name="issue"]')

    assert name_input.get_attribute("maxlength") == "100"
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
    assert issue_input.get_attribute("maxlength") == "1000"
