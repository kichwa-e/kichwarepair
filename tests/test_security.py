import pytest
import pathlib

def test_security_headers_and_validation(page):
    # Setup routing to allow file requests and Tailwind CDN
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    # Catch console errors (excluding expected favicon/logo errors)
    errors = []
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' and 'favicon' not in msg.text and 'logo' not in msg.text and 'ERR_FILE_NOT_FOUND' not in msg.text else None)

    # Test kichwa-connect.html
    connect_uri = pathlib.Path('kichwa-connect.html').resolve().as_uri()
    page.goto(connect_uri, wait_until='domcontentloaded')
    page.wait_for_timeout(1000)
    assert not errors, f"Console errors in kichwa-connect.html: {errors}"

    # Test kichwa_repair_with_blue_green_logo.html
    repair_uri = pathlib.Path('kichwa_repair_with_blue_green_logo.html').resolve().as_uri()
    page.goto(repair_uri, wait_until='domcontentloaded')
    page.wait_for_timeout(1000)
    assert not errors, f"Console errors in repair page: {errors}"

    # Verify input validation attributes
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute('maxlength') == '100'

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute('maxlength') == '20'
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$"

    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute('maxlength') == '1000'
