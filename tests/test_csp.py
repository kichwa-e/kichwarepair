import pytest
from playwright.sync_api import Page
import pathlib

def test_csp_exists(page: Page):
    file_path = pathlib.Path("kichwa-connect.html").resolve().as_uri()
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') else r.abort())
    page.goto(file_path)

    meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
    assert meta.count() == 1

    csp = meta.get_attribute('content')
    assert "default-src 'self'" in csp
    assert "script-src 'none'" in csp
