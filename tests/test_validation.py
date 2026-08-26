import pathlib
from playwright.sync_api import Page, expect

def test_form_validation(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path)

    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "20")
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute("maxlength", "1000")
