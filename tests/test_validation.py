import os
import pytest
from playwright.sync_api import Page, expect

def test_form_validation(page: Page):
    file_path = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(file_path)
    expect(page.locator('input[name="name"]')).to_have_attribute("maxlength", "100")
    expect(page.locator('input[name="phone"]')).to_have_attribute("maxlength", "20")
    expect(page.locator('textarea[name="issue"]')).to_have_attribute("maxlength", "1000")
