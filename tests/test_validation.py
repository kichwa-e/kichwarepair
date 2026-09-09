import os

def test_form_validation(page):
    file_path = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "cdn.tailwindcss.com" in route.request.url else route.abort())
    page.goto(file_path)

    # Assert name has maxlength="100"
    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    # Assert phone has maxlength="20" and pattern
    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    # Assert issue has maxlength="1000"
    issue_textarea = page.locator('textarea[name="issue"]')
    assert issue_textarea.get_attribute("maxlength") == "1000"
