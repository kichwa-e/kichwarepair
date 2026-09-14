import asyncio
import os
from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_form_validation():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_path = os.path.abspath("kichwa_repair_with_blue_green_logo.html")
        await page.goto(f"file://{file_path}")

        name_input = page.locator('input[name="name"]')
        phone_input = page.locator('input[name="phone"]')
        issue_textarea = page.locator('textarea[name="issue"]')

        assert await name_input.get_attribute("maxlength") == "100"
        assert await phone_input.get_attribute("type") == "tel"
        assert await phone_input.get_attribute("maxlength") == "20"
        assert await phone_input.evaluate('el => el.getAttribute("pattern")') == r"^[\d\s\+\-\(\)]+$"
        assert await issue_textarea.get_attribute("maxlength") == "1000"

        await browser.close()
