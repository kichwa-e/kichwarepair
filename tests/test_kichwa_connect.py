import re
import os

def test_kichwa_connect_phone_numbers():
    file_path = "kichwa-connect.html"
    assert os.path.exists(file_path), f"File {file_path} not found"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check that placeholders are NOT present
    assert "07XXXXXXXX" not in content, "Placeholder '07XXXXXXXX' found in file"
    assert "2547XXXXXXXX" not in content, "Placeholder '2547XXXXXXXX' found in file"

    # Check that correct numbers ARE present in the correct contexts
    # Tel link: tel:0701581233
    tel_pattern = re.compile(r'href="tel:0701581233"')
    assert tel_pattern.search(content), "Correct tel link 'href=\"tel:0701581233\"' not found"

    # WhatsApp link: https://wa.me/254701581233
    wa_pattern = re.compile(r'href="https://wa\.me/254701581233"')
    assert wa_pattern.search(content), "Correct WhatsApp link 'href=\"https://wa.me/254701581233\"' not found"
