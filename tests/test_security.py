import pathlib
from playwright.sync_api import Page, expect

def test_kichwa_connect_csp(page: Page):
    file_path = pathlib.Path(__file__).parent.parent / 'kichwa-connect.html'
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') else r.abort())

    errors = []
    page.on('pageerror', lambda e: errors.append(e.message))
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' and 'favicon.ico' not in msg.text else None)

    page.goto(file_path.resolve().as_uri())

    csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
    expect(csp_meta).to_have_count(1)

    expected_csp = "default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'self';"
    assert csp_meta.evaluate('el => el.getAttribute("content")') == expected_csp

    assert len(errors) == 0, f"Unexpected errors found: {errors}"
