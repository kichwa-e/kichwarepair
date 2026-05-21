import pathlib
from playwright.sync_api import sync_playwright

def test_mobile_menu_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        def handle_route(route):
            url = route.request.url
            if url.startswith("file://") or "cdn.tailwindcss.com" in url:
                route.continue_()
            else:
                route.abort()
        page.route("**/*", handle_route)

        file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve()
        file_uri = file_path.as_uri()

        page.goto(file_uri)

        mobile_menu = page.locator("#mobileMenu")
        menu_btn = page.locator("#menuBtn")

        # Initial state: hidden
        assert mobile_menu.evaluate("el => el.classList.contains('hidden')") is True, "Menu should be hidden initially"

        # Click to open
        menu_btn.click()
        assert mobile_menu.evaluate("el => el.classList.contains('hidden')") is False, "Menu should be visible after click"

        # Click to close
        menu_btn.click()
        assert mobile_menu.evaluate("el => el.classList.contains('hidden')") is True, "Menu should be hidden after second click"

        browser.close()
