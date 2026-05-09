const { test, expect } = require('@playwright/test');
const path = require('path');

test('footer year dynamically updates', async ({ page }) => {
  // Route to avoid timeouts when assets fail to load
  await page.route('**/*', (route) => {
    if (route.request().url().startsWith('file://') || route.request().url().includes('cdn.tailwindcss.com')) {
      return route.continue();
    }
    return route.abort();
  });

  // Get local file URI using relative path to robustly locate the HTML
  const filePath = path.resolve(__dirname, '../kichwa_repair_with_blue_green_logo.html');
  const fileUri = `file://${filePath}`;

  // Load page using domcontentloaded
  await page.goto(fileUri, { waitUntil: 'domcontentloaded' });

  // Get current year
  const currentYear = new Date().getFullYear().toString();

  // Check the year element text matches current year
  const yearElement = page.locator('#year');
  await expect(yearElement).toHaveText(currentYear);
});
