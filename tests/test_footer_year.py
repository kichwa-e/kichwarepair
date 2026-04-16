import os
import pytest
import pathlib
import datetime
from playwright.sync_api import sync_playwright

def test_footer_year():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") else route.abort())

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "kichwa_repair_with_blue_green_logo.html")
        file_uri = pathlib.Path(file_path).resolve().as_uri()

        page.goto(file_uri, wait_until='domcontentloaded')

        year_element = page.locator('#year')
        current_year = str(datetime.datetime.now().year)

        assert year_element.text_content() == current_year

        browser.close()
