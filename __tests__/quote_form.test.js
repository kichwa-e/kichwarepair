const fs = require('fs');
const path = require('path');
const { TextEncoder, TextDecoder } = require('util');
global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;
const { JSDOM } = require('jsdom');

const html = fs.readFileSync(path.resolve(__dirname, '../kichwa_repair_with_blue_green_logo.html'), 'utf8');

describe('Quote Form', () => {
  let dom;
  let document;

  beforeEach(() => {
    dom = new JSDOM(html);
    document = dom.window.document;
  });

  test('should have a form named "quote"', () => {
    const form = document.querySelector('form[name="quote"]');
    expect(form).not.toBeNull();
  });

  test('should have a required name input', () => {
    const nameInput = document.querySelector('input[name="name"]');
    expect(nameInput).not.toBeNull();
    expect(nameInput.hasAttribute('required')).toBe(true);
  });

  test('should have a required phone input', () => {
    const phoneInput = document.querySelector('input[name="phone"]');
    expect(phoneInput).not.toBeNull();
    expect(phoneInput.hasAttribute('required')).toBe(true);
  });

  test('should have a required issue textarea', () => {
    const issueInput = document.querySelector('textarea[name="issue"]');
    expect(issueInput).not.toBeNull();
    expect(issueInput.hasAttribute('required')).toBe(true);
  });
});
