import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_kichwa_connect_csp(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / "kichwa-connect.html"
    page.goto(file_path.resolve().as_uri())

    csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
    expect(csp_meta).to_have_count(1)

    csp_content = csp_meta.evaluate('el => el.getAttribute("content")')
    assert "default-src 'self'" in csp_content
    assert "script-src 'none'" in csp_content
