// Kichwa Repair Technology Contact Configuration

const contactConfig = {
    phoneDisplay: '0701581233',
    phoneTel: '0701581233', // Used in tel: links
    whatsapp: '254701581233', // Used in wa.me links
    email: 'hello@kichwarepair.co.ke'
};

function updateContactInfo() {
    // Update phone links (tel:)
    document.querySelectorAll('.js-phone-link').forEach(el => {
        el.href = `tel:${contactConfig.phoneTel}`;
    });

    // Update displayed phone number text
    document.querySelectorAll('.js-phone-text').forEach(el => {
        el.textContent = contactConfig.phoneDisplay;
    });

    // Update WhatsApp links
    document.querySelectorAll('.js-whatsapp-link').forEach(el => {
        el.href = `https://wa.me/${contactConfig.whatsapp}`;
    });

    // Update Email links
    document.querySelectorAll('.js-email-link').forEach(el => {
        el.href = `mailto:${contactConfig.email}`;
        // If the element has a specific data attribute, update text too
        if (el.dataset.updateText === 'true') {
            el.textContent = contactConfig.email;
        }
    });

    // Attempt to update JSON-LD schema
    const schemaScript = document.querySelector('script[type="application/ld+json"]');
    if (schemaScript) {
        try {
            const schema = JSON.parse(schemaScript.textContent);
            if (schema['@type'] === 'LocalBusiness' || schema['@type'] === 'Organization') {
                schema.telephone = contactConfig.phoneDisplay;
                // schema.email could be added if supported by schema type
                schemaScript.textContent = JSON.stringify(schema, null, 2);
            }
        } catch (e) {
            console.error('Error updating schema:', e);
        }
    }
}

// Run on load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateContactInfo);
} else {
    updateContactInfo();
}
