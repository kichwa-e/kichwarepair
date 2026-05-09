import os
import pathlib
import pytest
from playwright.sync_api import sync_playwright

def test_quote_form_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        def handle_route(route):
            request = route.request
            if request.method == "POST":
                route.fulfill(status=200, body="Mock Netlify Success", content_type="text/html")
            elif request.url.startswith("file://") or "cdn.tailwindcss.com" in request.url:
                route.continue_()
            else:
                route.abort()

        page.route("**/*", handle_route)

        file_path = os.path.abspath("kichwa_repair_with_blue_green_logo.html")
        page.goto(pathlib.Path(file_path).as_uri(), wait_until="domcontentloaded")

        page.fill("input[name='name']", "John Doe")
        page.fill("input[name='phone']", "+254712345678")
        page.fill("textarea[name='issue']", "Broken screen")

        with page.expect_response(lambda response: response.status == 200) as response_info:
            page.click("button[type='submit']")

        assert "Mock Netlify Success" in response_info.value.text()

        browser.close()
