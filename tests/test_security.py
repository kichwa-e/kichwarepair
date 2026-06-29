import pathlib
from playwright.sync_api import Page, expect

def test_kichwa_connect_csp(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / "kichwa-connect.html"
    page.goto(file_path.resolve().as_uri())

    csp_meta = page.locator("meta[http-equiv='Content-Security-Policy']")
    expect(csp_meta).to_have_count(1)

    content = csp_meta.evaluate("el => el.getAttribute('content')")
    expected_content = "default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'self';"
    assert content == expected_content
