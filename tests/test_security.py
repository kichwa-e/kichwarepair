import pytest
from playwright.sync_api import Page
import os

def test_security_validation(page: Page):
    file_path = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(file_path)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_textarea = page.locator('textarea[name="issue"]')

    assert name_input.get_attribute('maxlength') == "100"
    assert name_input.evaluate('el => el.getAttribute("pattern")') == "^[a-zA-Z\\s\\-']+$"

    assert phone_input.get_attribute('maxlength') == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == "^[\\d\\s\\+\\-\\(\\)]+$"

    assert issue_textarea.get_attribute('maxlength') == "1000"
