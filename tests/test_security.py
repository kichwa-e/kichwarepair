from playwright.sync_api import Page, expect
import pathlib

def test_form_input_validation(page: Page):
    file_uri = pathlib.Path(__file__).parent.parent.joinpath('kichwa_repair_with_blue_green_logo.html').resolve().as_uri()

    # Allow local file and tailwind CDN requests
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(file_uri)

    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute("maxlength", "100")

    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute("maxlength", "20")
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_input = page.locator('textarea[name="issue"]')
    expect(issue_input).to_have_attribute("maxlength", "1000")
