import pytest
from playwright.sync_api import Page
import pathlib

def test_csp_and_scripts(page: Page):
    file_path = pathlib.Path("kichwa_repair_with_blue_green_logo.html").resolve().as_uri()

    errors = []
    page.on("pageerror", lambda err: errors.append(err))

    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    page.goto(file_path)
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]').get_attribute('content')
    assert "unsafe-inline" not in csp_meta.split("script-src")[1].split(";")[0], "CSP still contains unsafe-inline for scripts"

    assert page.locator('script[src="tailwind-config.js"]').count() == 1
    assert page.locator('script[src="app.js"]').count() == 1

    assert len(errors) == 0, f"Page had errors: {errors}"
