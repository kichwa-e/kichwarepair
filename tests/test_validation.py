import pytest
from playwright.sync_api import Page

def test_input_validation(page: Page):
    page.goto(f"file://{__import__('os').path.abspath('kichwa_repair_with_blue_green_logo.html')}")

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_input = page.locator('textarea[name="issue"]')

    assert name_input.get_attribute("maxlength") == "100"

    assert phone_input.get_attribute("maxlength") == "20"
    # Use evaluate to handle potential python escape issues
    assert page.evaluate('() => document.querySelector("input[name=\'phone\']").getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    assert issue_input.get_attribute("maxlength") == "1000"
