import os
from playwright.sync_api import expect

def test_form_validation(page):
    current_dir = os.getcwd()
    page.goto(f"file://{current_dir}/kichwa_repair_with_blue_green_logo.html")

    # Wait for form to load
    page.wait_for_selector('form[name="quote"]')

    # Check Name field
    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    # Check Phone field
    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "20")
    # Retrieve pattern attribute directly using JS evaluation to avoid regex escaping mismatch
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    # Check Issue field
    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
