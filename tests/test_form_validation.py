import pathlib

def test_form_validation(page):
    file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'
    uri = file_path.resolve().as_uri()

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(uri)
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute('maxlength') == '100', "Name maxlength not set"

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute('maxlength') == '20', "Phone maxlength not set"
    pattern = phone_input.evaluate('el => el.getAttribute("pattern")')
    assert pattern == r"^[\d\s\+\-\(\)]+$", f"Phone pattern is incorrect: {pattern}"

    issue_input = page.locator('textarea[name="issue"]')
    assert issue_input.get_attribute('maxlength') == '1000', "Issue maxlength not set"
