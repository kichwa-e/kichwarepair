import pytest
from playwright.sync_api import sync_playwright, Page
import os
import pathlib

@pytest.fixture(scope="module")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_homepage_loads(page: Page):
    # Construct the absolute file path
    # tests/test_landing_page.py -> tests/ -> root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, "kichwa_repair_with_blue_green_logo.html")

    # Check if file exists
    assert os.path.exists(file_path), f"File not found: {file_path}"

    # Load the page using pathlib for robust URI creation
    page_url = pathlib.Path(file_path).as_uri()
    page.goto(page_url)

    # Assertions
    # Title
    assert page.title() == "Kichwa Repair Technology | Fast Phone Repair in Nairobi"

    # Main Heading
    # Using a text selector which is robust
    heading = page.get_by_role("heading", name="Fast, Honest Phone Repair in Nairobi")
    assert heading.is_visible()

    # Button
    # We can search for the link with text "Book on WhatsApp"
    button = page.get_by_role("link", name="Book on WhatsApp").first
    assert button.is_visible()
