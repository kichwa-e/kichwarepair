import pytest
from playwright.sync_api import Page, expect
import os

def test_form_input_validation(page: Page):
    workspace_dir = os.path.abspath(os.getcwd())
    page.goto(f"file://{workspace_dir}/kichwa_repair_with_blue_green_logo.html")

    name_input = page.locator('input[name="name"]')
    phone_input = page.locator('input[name="phone"]')
    issue_textarea = page.locator('textarea[name="issue"]')

    expect(name_input).to_have_attribute('maxlength', '100')
    expect(phone_input).to_have_attribute('maxlength', '20')

    phone_pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert phone_pattern == r"^[\d\s\+\-\(\)]+$"

    expect(issue_textarea).to_have_attribute('maxlength', '1000')
