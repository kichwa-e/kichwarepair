import pytest
from playwright.sync_api import Page, expect
from pathlib import Path

def test_kichwa_connect_page_load(page: Page):
    """
    Test that the Kichwa Connect page loads successfully and displays key elements.
    """
    # Determine the absolute path to the HTML file relative to the repo root
    base_dir = Path(__file__).parent.parent
    file_path = (base_dir / "kichwa-connect.html").resolve()

    # Check if file exists
    assert file_path.exists(), f"File not found: {file_path}"

    # Load the page using the file protocol
    page.goto(file_path.as_uri())

    # Verify the title
    expect(page).to_have_title("Kichwa Connect | Fast Internet, Repair & Support")

    # Verify the main header
    expect(page.locator("h1")).to_have_text("KICHWA CONNECT")

    # Verify the services section exists
    expect(page.locator("h2", has_text="Our Services")).to_be_visible()

    # Verify at least one service card is visible
    expect(page.locator(".card").first).to_be_visible()
