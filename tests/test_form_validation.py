import pytest
import pathlib

def test_form_validation(page):
    file_path = pathlib.Path.cwd() / "kichwa_repair_with_blue_green_logo.html"
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(file_path.resolve().as_uri())

    # Check name field
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    # Check phone field
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    # Check issue field
    issue_input = page.locator('textarea[name="issue"]')
    assert issue_input.get_attribute("maxlength") == "1000"
