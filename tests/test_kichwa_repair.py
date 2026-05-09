import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_kichwa_repair_page_loads(page: Page):
    """
    Verifies that the Kichwa Repair landing page loads correctly
    and displays key elements.
    """
    # Construct absolute path to the HTML file
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").absolute()
    url = f"file://{file_path}"

    # Navigate to the page
    page.goto(url)

    # Check title
    expect(page).to_have_title("Kichwa Repair Technology | Fast Phone Repair in Nairobi")

    # Check H1 - The text might be split across lines in the source, but playwright handles text content nicely
    h1 = page.locator("h1")
    expect(h1).to_contain_text("Fast, Honest Phone Repair in Nairobi")

    # Check WhatsApp button
    # There are multiple "Book on WhatsApp" links, we can check that at least one is visible
    whatsapp_btns = page.get_by_role("link", name="Book on WhatsApp")
    expect(whatsapp_btns.first).to_be_visible()
    expect(whatsapp_btns.first).to_have_attribute("href", "https://wa.me/254701581233")
