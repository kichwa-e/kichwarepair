import pytest
from playwright.sync_api import sync_playwright, expect
import pathlib
import re

def test_mobile_menu_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Ensure we are testing in a mobile viewport so the button and menu are relevant
        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        # Route requests to abort everything except local files and required CDNs
        page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") else route.abort())

        file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()
        page.goto(file_path)

        menu_btn = page.locator("#menuBtn")
        mobile_menu = page.locator("#mobileMenu")

        # In Tailwind, 'hidden' (exact class) hides on mobile, 'md:hidden' hides on tablet+.
        # We want to verify the exact class 'hidden' is toggled.
        # Note: expect(...).not_to_have_class(regex) tests against the FULL string.
        # For md:hidden, the regex \bhidden\b matches "hidden" inside "md:hidden" (since : is a word boundary in regex).
        # We should use a lookbehind or negative lookbehind, or just regex checking for whitespace or start/end of string.
        # Actually, since it splits by space, let's just use Python asserts on the split array, it's more accurate for exact class names.
        # OR use evaluate to get classList.contains('hidden')

        # Another approach: Playwright expect API for class actually doesn't check array but the full string.
        # We can just check evaluate

        def assert_has_hidden_class(has_hidden):
            has_class = mobile_menu.evaluate("el => el.classList.contains('hidden')")
            assert has_class == has_hidden

        # Initially, the mobile menu should have the 'hidden' class
        assert_has_hidden_class(True)

        # Click the menu button
        menu_btn.click()

        # The 'hidden' class should be removed
        assert_has_hidden_class(False)

        # Click the menu button again
        menu_btn.click()

        # The 'hidden' class should be added back
        assert_has_hidden_class(True)

        browser.close()
