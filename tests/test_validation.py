import os
from playwright.sync_api import Page, expect
import re

def test_form_validation(page: Page):
    file_path = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(file_path)

    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "20")

    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
