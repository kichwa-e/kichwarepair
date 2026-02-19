const { initApp } = require('../assets/js/main.js');

describe('Mobile Menu Toggle', () => {
    let menuBtn;
    let mobileMenu;
    let yearElement;

    beforeEach(() => {
        // Reset DOM
        document.body.innerHTML = `
            <button id="menuBtn"></button>
            <div id="mobileMenu" class="hidden"></div>
            <span id="year"></span>
        `;
        menuBtn = document.getElementById('menuBtn');
        mobileMenu = document.getElementById('mobileMenu');
        yearElement = document.getElementById('year');
    });

    test('toggles mobile menu visibility on button click', () => {
        initApp();

        // Initial state: hidden
        expect(mobileMenu.classList.contains('hidden')).toBe(true);

        // Click to open
        menuBtn.click();
        expect(mobileMenu.classList.contains('hidden')).toBe(false);

        // Click to close
        menuBtn.click();
        expect(mobileMenu.classList.contains('hidden')).toBe(true);
    });

    test('sets the current year in footer', () => {
        initApp();
        const currentYear = new Date().getFullYear().toString();
        expect(yearElement.textContent).toBe(currentYear);
    });

    test('does not throw if elements are missing', () => {
        document.body.innerHTML = ''; // Empty DOM
        expect(() => initApp()).not.toThrow();
    });
});
