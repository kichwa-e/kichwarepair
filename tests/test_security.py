import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_csp_no_inline_scripts(page: Page):
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    html_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'

    errors = []
    page.on("pageerror", lambda err: errors.append(err.message))
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" and "ERR_FILE_NOT_FOUND" not in msg.text and "ERR_FAILED" not in msg.text else None)

    page.set_viewport_size({"width": 375, "height": 667})
    page.goto(html_path.resolve().as_uri())

    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    for error in errors:
        assert "Content Security Policy" not in error, f"CSP Error: {error}"

    menu_btn = page.locator('#menuBtn')
    mobile_menu = page.locator('#mobileMenu')

    expect(menu_btn).to_be_visible()
    assert mobile_menu.evaluate('node => node.classList.contains("hidden")')

    menu_btn.click()
    assert not mobile_menu.evaluate('node => node.classList.contains("hidden")')

    body = page.locator('body')
    bg_color = body.evaluate('node => window.getComputedStyle(node).backgroundColor')
    assert bg_color != "rgba(0, 0, 0, 0)"
