import pathlib

def test_form_validation(page):
    file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'

    # Block non-file and non-tailwind requests to speed up tests
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(file_path.resolve().as_uri())

    # Ensure page is loaded
    page.wait_for_load_state('domcontentloaded')

    # Verify Name field
    name_field = page.locator('input[name="name"]')
    assert name_field.get_attribute('maxlength') == '100'

    # Verify Phone field
    phone_field = page.locator('input[name="phone"]')
    assert phone_field.get_attribute('maxlength') == '20'
    assert phone_field.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    # Verify Issue field
    issue_field = page.locator('textarea[name="issue"]')
    assert issue_field.get_attribute('maxlength') == '1000'
