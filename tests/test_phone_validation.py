import os
import re
from playwright.sync_api import sync_playwright

def test_phone_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the file
        file_path = os.path.abspath("kichwa_repair_with_blue_green_logo.html")
        page.goto(f"file://{file_path}")

        # Locate the input
        phone_input = page.locator('input[name="phone"]')

        # Check type attribute
        type_attr = phone_input.get_attribute("type")
        print(f"type attribute: {type_attr}")
        if type_attr != "tel":
            print("FAIL: type attribute is not 'tel'")
        else:
            print("PASS: type attribute is 'tel'")

        # Check pattern attribute
        pattern_attr = phone_input.get_attribute("pattern")
        print(f"pattern attribute: {pattern_attr}")
        expected_pattern = r"[0-9+ \-]{10,20}"
        if pattern_attr != expected_pattern:
             print(f"FAIL: pattern attribute '{pattern_attr}' does not match expected '{expected_pattern}'")
        else:
             print("PASS: pattern attribute matches expected")

        # Verify strict compliance
        if type_attr == "tel" and pattern_attr == expected_pattern:
            print("VERIFICATION SUCCESS: Phone input is secure.")
        else:
            print("VERIFICATION FAILURE: Phone input is insecure.")

        browser.close()

if __name__ == "__main__":
    test_phone_validation()
