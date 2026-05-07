import os
import json
import pathlib
import pytest
from playwright.sync_api import Page, sync_playwright

def test_schema_parsing():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'kichwa_repair_with_blue_green_logo.html'))
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.route("**/*", lambda route: route.continue_() if route.request.url.startswith("file://") else route.abort())
        page.goto(pathlib.Path(file_path).resolve().as_uri())
        schema_text = page.locator('script[type="application/ld+json"]').text_content()
        schema_json = json.loads(schema_text)
        assert schema_json['@type'] == 'LocalBusiness'
        assert 'sameAs' not in schema_json
        browser.close()
