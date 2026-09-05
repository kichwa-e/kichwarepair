import os
import pytest
from playwright.sync_api import Page

def test_form_validation(page: Page):
    file_path = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(file_path)

    # Test name field
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute('maxlength') == '100'
    assert name_input.get_attribute('required') is not None

    # Test phone field
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute('maxlength') == '20'
    assert phone_input.get_attribute('required') is not None

    # Using evaluate to avoid unicode escape issues
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    # Test issue field
    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute('maxlength') == '1000'
