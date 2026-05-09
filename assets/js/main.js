function initApp() {
    // Mobile menu toggle
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    menuBtn?.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));

    // Year in footer
    const yearElement = document.getElementById('year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}

// Check if running in Node.js environment for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initApp };
} else {
    // Browser environment
    initApp();
}
