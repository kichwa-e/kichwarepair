import os
import pathlib
import pytest
from playwright.sync_api import sync_playwright

def test_quote_form_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Handle missing assets and third-party requests
        def handle_console(msg):
            pass

        page.on("console", handle_console)

        # Route requests
        def handle_route(route):
            request = route.request
            # Mock Netlify POST request
            if request.method == "POST":
                route.fulfill(status=200, body="Mocked Netlify response", content_type="text/html")
            # Abort external non-file requests to speed up/avoid timeouts if needed
            elif request.url.startswith("file://") or "cdn.tailwindcss.com" in request.url:
                route.continue_()
            else:
                route.abort()

        page.route("**/*", handle_route)

        # Load file
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kichwa_repair_with_blue_green_logo.html')
        file_uri = pathlib.Path(file_path).resolve().as_uri()
        page.goto(file_uri)

        # Fill form
        page.fill('input[name="name"]', 'John Doe')
        page.fill('input[name="phone"]', '254701581233')
        page.fill('textarea[name="issue"]', 'Broken screen')

        with page.expect_request(lambda request: request.method == "POST") as request_info:
            page.click('button[type="submit"]')

        request = request_info.value
        assert request.method == "POST"
        post_data = request.post_data

        assert "John+Doe" in post_data or "John Doe" in post_data
        assert "254701581233" in post_data
        assert "Broken+screen" in post_data or "Broken screen" in post_data

        browser.close()
