import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_csp_header(page: Page):
    file_path = pathlib.Path("kichwa-connect.html").resolve().as_uri()

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') else r.abort())
    page.goto(file_path)

    meta_tag = page.locator('meta[http-equiv="Content-Security-Policy"]')
    expect(meta_tag).to_have_attribute("content", "default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'self';")
