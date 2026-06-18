import pytest
from playwright.sync_api import Page, expect
import pathlib

def test_csp_and_external_scripts(page: Page):
    # Route interception for external CDN and file access
    page.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') or r.request.url.startswith('https://cdn.tailwindcss.com') else r.abort())

    file_path = pathlib.Path(__file__).parent.parent / 'kichwa_repair_with_blue_green_logo.html'
    page.goto(file_path.resolve().as_uri())

    # Wait for DOM and Tailwind processing
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(1000)

    # Verify no inline scripts by checking CSP meta tag
    csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
    csp_content = csp_meta.get_attribute("content")
    assert "'unsafe-inline'" not in csp_content.split("script-src")[1].split(";")[0], "CSP still allows inline scripts"

    # Verify app.js loaded and works (mobile menu toggle)
    page.set_viewport_size({"width": 375, "height": 667})
    menu_btn = page.locator('#menuBtn')
    mobile_menu = page.locator('#mobileMenu')

    # Check if 'hidden' class is present using evaluate
    is_hidden = mobile_menu.evaluate('node => node.classList.contains("hidden")')
    assert is_hidden, "Mobile menu should be hidden initially"

    menu_btn.click()

    is_hidden_after_click = mobile_menu.evaluate('node => node.classList.contains("hidden")')
    assert not is_hidden_after_click, "Mobile menu should not be hidden after click"

    # Verify tailwind loaded (computed style)
    body = page.locator('body')
    bg_color = body.evaluate('node => window.getComputedStyle(node).getPropertyValue("background-color")')
    assert bg_color != "rgba(0, 0, 0, 0)", "Tailwind CSS failed to load"
