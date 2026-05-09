from playwright.sync_api import sync_playwright
import os

def test_form_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        filepath = os.path.abspath("kichwa_repair_with_blue_green_logo.html")
        page.goto(f"file://{filepath}")

        # Test Name Field
        name_input = page.locator('input[name="name"]')
        assert name_input.get_attribute("maxlength") == "50", "Name field is missing maxlength=50"

        # Test Phone Field
        phone_input = page.locator('input[name="phone"]')
        assert phone_input.get_attribute("type") == "tel", "Phone field should be type=tel"
        assert phone_input.get_attribute("pattern") == "[0-9+ \-]{10,20}", "Phone field pattern is incorrect"
        assert phone_input.get_attribute("maxlength") == "20", "Phone field is missing maxlength=20"

        # Test Issue Field
        issue_input = page.locator('textarea[name="issue"]')
        assert issue_input.get_attribute("maxlength") == "500", "Issue field is missing maxlength=500"

        print("All ad-hoc form validation tests passed!")
        browser.close()

if __name__ == "__main__":
    test_form_validation()
