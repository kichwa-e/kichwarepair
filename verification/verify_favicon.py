from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Determine the absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/kichwa_repair_with_blue_green_logo.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Check for the favicon link
        favicon_link = page.query_selector('link[rel="icon"]')

        if favicon_link:
            href = favicon_link.get_attribute('href')
            type_attr = favicon_link.get_attribute('type')
            print(f"Found favicon link: href='{href}', type='{type_attr}'")

            if href == "favicon.svg" and type_attr == "image/svg+xml":
                print("Favicon verification PASSED.")
            else:
                print("Favicon verification FAILED: Incorrect href or type.")
        else:
            print("Favicon verification FAILED: Link tag not found.")

        # Take a screenshot
        page.screenshot(path="verification/favicon_verification.png")
        print("Screenshot saved to verification/favicon_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
