import os
from playwright.sync_api import sync_playwright

def verify_contact_info():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath("kichwa_repair_with_blue_green_logo.html")
        page.goto(f"file://{file_path}")

        # Check Phone Link in Top Bar
        # There are multiple phone links, let's check the first one (top bar)
        phone_link = page.locator('a[data-contact-link="phone"]').first
        href = phone_link.get_attribute("href")
        text = phone_link.inner_text()
        print(f"Phone Link Href: {href}")
        print(f"Phone Link Text: {text}")

        if href != "tel:0701581233":
            print("FAILED: Phone link href incorrect")

        if "0701581233" not in text:
             print("FAILED: Phone link text incorrect")

        # Check WhatsApp Link
        whatsapp_link = page.locator('a[data-contact-link="whatsapp"]').first
        wa_href = whatsapp_link.get_attribute("href")
        print(f"WhatsApp Link Href: {wa_href}")

        if wa_href != "https://wa.me/254701581233":
            print("FAILED: WhatsApp link href incorrect")

        # Take screenshot
        page.screenshot(path="verification/contact_info.png")
        print("Screenshot saved to verification/contact_info.png")

        browser.close()

if __name__ == "__main__":
    verify_contact_info()
