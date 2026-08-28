from playwright.sync_api import Page
import os

def test_input_validation(page: Page):
    file_path = f"file://{os.path.abspath('kichwa_repair_with_blue_green_logo.html')}"
    page.goto(file_path)

    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_input = page.locator('textarea[name="issue"]')
    assert issue_input.get_attribute("maxlength") == "1000"
