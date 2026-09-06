import os

def test_form_validation(page):
    page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") or "cdn.tailwindcss.com" in route.request.url else route.abort())
    page.goto(f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html")

    name_input = page.locator('input[name="name"]')
    assert name_input.get_attribute("maxlength") == "100"

    phone_input = page.locator('input[name="phone"]')
    assert phone_input.get_attribute("maxlength") == "20"
    assert phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"

    issue_input = page.locator('textarea[name="issue"]')
    assert issue_input.get_attribute("maxlength") == "1000"
