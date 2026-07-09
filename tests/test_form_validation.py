import pytest
from playwright.sync_api import Page, expect
import pathlib

@pytest.fixture(scope="function")
def html_uri():
    file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'
    return file_path.resolve().as_uri()

def test_form_validation_attributes(page: Page, html_uri):
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
    page.goto(html_uri)

    name_input = page.locator('input[name="name"]')
    expect(name_input).to_have_attribute('maxlength', '100')

    phone_input = page.locator('input[name="phone"]')
    expect(phone_input).to_have_attribute('maxlength', '20')

    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    expect(issue_textarea).to_have_attribute('maxlength', '1000')
