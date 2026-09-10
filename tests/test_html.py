import os
def test_form_attributes(page):
    filepath = f"file://{os.getcwd()}/kichwa_repair_with_blue_green_logo.html"
    page.goto(filepath)
    name_el = page.locator('input[name="name"]')
    assert name_el.get_attribute("maxlength") == "100"
    phone_el = page.locator('input[name="phone"]')
    assert phone_el.get_attribute("maxlength") == "20"
    assert phone_el.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
    issue_el = page.locator('textarea[name="issue"]')
    assert issue_el.get_attribute("maxlength") == "1000"
