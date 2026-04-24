from playwright.sync_api import sync_playwright
import os
import pathlib

def test_csp_violations():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Track console errors (CSP violations show up here)
        errors = []
        def handle_console(msg):
            # Ignore missing logo.png which isn't part of this repo
            if msg.type == "error" and "logo.png" not in msg.text and "ERR_FILE_NOT_FOUND" not in msg.text:
                errors.append(msg.text)
        page.on("console", handle_console)

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kichwa_repair_with_blue_green_logo.html')
        file_uri = pathlib.Path(file_path).resolve().as_uri()

        # Need to allow CDNs for the test to work correctly
        page.goto(file_uri, wait_until="networkidle")

        # Assert no CSP errors
        assert len(errors) == 0, f"Found console errors: {errors}"

        browser.close()
