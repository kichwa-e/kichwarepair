import pathlib
from playwright.sync_api import sync_playwright

def test_quote_form_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        post_data_captured = []

        def handle_route(route):
            if route.request.method == "POST":
                post_data_captured.append(route.request.post_data)
                route.fulfill(status=200, body="Mock success")
            elif route.request.url.startswith("file://") or "cdn.tailwindcss.com" in route.request.url:
                route.continue_()
            else:
                route.abort()

        page.route("**/*", handle_route)

        # Resolve the relative path to the HTML file dynamically
        base_dir = pathlib.Path(__file__).parent.parent
        file_path = base_dir / "kichwa_repair_with_blue_green_logo.html"
        url = file_path.resolve().as_uri()
        page.goto(url)

        page.fill('input[name="name"]', "Test User")
        page.fill('input[name="phone"]', "1234567890")
        page.fill('textarea[name="issue"]', "Test issue description")

        with page.expect_request(lambda request: request.method == "POST") as request_info:
            page.click('button[type="submit"]')

        # Wait a small moment to ensure route handler fulfills the request completely before checking the captured list
        # Though `request_info` captures it, we also added it to `post_data_captured` in the route

        assert len(post_data_captured) == 1
        post_data = post_data_captured[0]

        assert "form-name=quote" in post_data
        assert "name=Test+User" in post_data
        assert "phone=1234567890" in post_data
        assert "issue=Test+issue+description" in post_data

        browser.close()
