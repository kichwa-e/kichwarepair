import os
from playwright.sync_api import Page

def test_form_validation(page: Page):
    page.goto(f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html")

    # Assert name field maxlength
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    # Assert phone field maxlength and pattern
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    # Assert issue field maxlength
    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute("maxlength") == "1000"
