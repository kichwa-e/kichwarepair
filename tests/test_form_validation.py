import pathlib
from playwright.sync_api import sync_playwright

def test_form_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'

        page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())
        page.goto(file_path.resolve().as_uri(), wait_until='domcontentloaded')
        page.wait_for_timeout(1000)

        name_input = page.locator('input[name="name"]')
        assert name_input.get_attribute('pattern') == r"^[a-zA-Z\xC0-\xFF\s\-'\.]+$"
        assert name_input.get_attribute('maxlength') == "100"

        phone_input = page.locator('input[name="phone"]')
        assert phone_input.get_attribute('pattern') == r"^[\d\s\+\-\(\)]+$"
        assert phone_input.get_attribute('maxlength') == "20"

        issue_input = page.locator('textarea[name="issue"]')
        assert issue_input.get_attribute('maxlength') == "1000"

        browser.close()
