const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('Kichwa Repair HTML Tests', () => {
  let dom;
  let document;

  beforeEach(() => {
    // Read the HTML file
    const htmlPath = path.resolve(__dirname, '../kichwa_repair_with_blue_green_logo.html');
    const html = fs.readFileSync(htmlPath, 'utf8');

    // Create a JSDOM instance
    dom = new JSDOM(html);
    document = dom.window.document;
  });

  test('Copyright year in footer is dynamic and correct', () => {
    // Locate the script that sets the year
    const scripts = document.querySelectorAll('script');
    let yearScriptContent = null;

    scripts.forEach(script => {
      if (script.textContent.includes("document.getElementById('year')")) {
        yearScriptContent = script.textContent;
      }
    });

    expect(yearScriptContent).not.toBeNull();

    // Execute the script content manually
    const runScript = new Function('document', yearScriptContent);
    runScript(document);

    // Verify the year
    const yearSpan = document.getElementById('year');
    const currentYear = new Date().getFullYear().toString();
    expect(yearSpan.textContent).toBe(currentYear);
  });
});
