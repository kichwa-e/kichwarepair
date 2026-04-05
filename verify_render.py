import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Route to block external requests but allow file:// and specific domains if needed
        await page.route("**/*", lambda route: route.continue_() if "file://" in route.request.url or "cdn.tailwindcss.com" in route.request.url else route.abort())

        # Load local HTML file
        await page.goto("file:///app/kichwa_repair_with_blue_green_logo.html", wait_until='domcontentloaded')

        # Check if basic layout renders correctly (e.g. title)
        title = await page.title()
        print(f"Title: {title}")

        await browser.close()

asyncio.run(main())
