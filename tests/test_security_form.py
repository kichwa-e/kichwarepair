import pathlib
from playwright.sync_api import Page, expect

def test_form_security_attributes(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve()
    page.goto(file_path.as_uri())

    # Check name field
    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    # Check phone field
    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "30")

    # Note: pattern check using getAttribute since expect().to_have_attribute has escaping issues with regex
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    # Check issue field
    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
