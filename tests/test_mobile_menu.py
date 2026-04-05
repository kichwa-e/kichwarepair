import pytest
from playwright.sync_api import sync_playwright
import os
from pathlib import Path
import datetime

# Use a relative path from the script directory to the HTML file
BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = (BASE_DIR / "kichwa_repair_with_blue_green_logo.html").as_uri()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def setup_page(browser, width, height):
    context = browser.new_context(viewport={"width": width, "height": height})
    page = context.new_page()

    # Block external resources completely to avoid timeouts in restricted environments
    def route_handler(route):
        url = route.request.url
        if url.startswith("file://"):
            route.continue_()
        else:
            route.abort()

    page.route("**/*", route_handler)

    # Inject minimal CSS to handle hidden/visible elements since Tailwind won't load
    # in restricted network environments.
    page.add_init_script("""
        window.addEventListener('DOMContentLoaded', () => {
            const style = document.createElement('style');
            style.innerHTML = `
                .hidden { display: none !important; }
                @media (min-width: 768px) {
                    .md\\\\:hidden { display: none !important; }
                }
            `;
            document.head.appendChild(style);
        });
    """)

    # Ensure the page loads successfully or fail the test
    response = page.goto(FILE_PATH, wait_until="commit", timeout=5000)
    if not response or not response.ok:
        pytest.fail(f"Failed to load {FILE_PATH}")

    return page, context

def test_mobile_menu_toggle(browser):
    page, context = setup_page(browser, 375, 667)

    page.wait_for_selector("#menuBtn", state="attached", timeout=5000)

    menu_btn = page.locator("#menuBtn")
    mobile_menu = page.locator("#mobileMenu")

    # Check if menu button is visible on mobile
    assert menu_btn.is_visible(), "Menu button should be visible on mobile"

    # Check if mobile menu is initially hidden
    assert mobile_menu.is_hidden(), "Mobile menu should be initially hidden"

    # Click menu button
    menu_btn.click()

    # Check if mobile menu is now visible
    assert mobile_menu.is_visible(), "Mobile menu should be visible after clicking menu button"

    # Click menu button again
    menu_btn.click()

    # Check if mobile menu is hidden again
    assert mobile_menu.is_hidden(), "Mobile menu should be hidden after clicking menu button again"

    context.close()

def test_menu_button_visibility_on_desktop(browser):
    page, context = setup_page(browser, 1280, 800)

    page.wait_for_selector("#menuBtn", state="attached", timeout=5000)
    menu_btn = page.locator("#menuBtn")

    # On desktop, menuBtn should be hidden (md:hidden)
    assert not menu_btn.is_visible(), "Menu button should be hidden on desktop"

    context.close()

def test_footer_year(browser):
    page, context = setup_page(browser, 1280, 800)

    page.wait_for_selector("#year", state="attached", timeout=5000)
    year_span = page.locator("#year")
    current_year = str(datetime.datetime.now().year)

    assert year_span.text_content() == current_year, f"Footer year should be {current_year}"

    context.close()
