import os
from playwright.sync_api import Page, expect

def test_form_validation(page: Page):
    filepath = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(filepath)

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_textarea = page.locator('textarea[name="issue"]')

    expect(name_input).to_have_attribute("maxlength", "100")
    expect(phone_input).to_have_attribute("maxlength", "20")
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
