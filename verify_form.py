import re
from html.parser import HTMLParser

class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.textareas = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "input":
            if attr_dict.get("name") in ["name", "phone"]:
                self.inputs.append(attr_dict)
        elif tag == "textarea":
            if attr_dict.get("name") == "issue":
                self.textareas.append(attr_dict)

def test_form_validation():
    with open('kichwa_repair_with_blue_green_logo.html', 'r', encoding='utf-8') as f:
        html = f.read()

    parser = FormParser()
    parser.feed(html)

    name_input = next((i for i in parser.inputs if i.get("name") == "name"), None)
    assert name_input is not None, "Name input not found"
    assert name_input.get("maxlength") == "100", f"Expected maxlength 100 on name, got {name_input.get('maxlength')}"
    assert "required" in name_input, "Expected required attribute on name"

    phone_input = next((i for i in parser.inputs if i.get("name") == "phone"), None)
    assert phone_input is not None, "Phone input not found"
    assert phone_input.get("type") == "tel", f"Expected type tel on phone, got {phone_input.get('type')}"
    assert phone_input.get("pattern") == r"[0-9+ \-]{10,20}", f"Expected pattern on phone, got {phone_input.get('pattern')}"
    assert phone_input.get("maxlength") == "20", f"Expected maxlength 20 on phone, got {phone_input.get('maxlength')}"
    assert "required" in phone_input, "Expected required attribute on phone"

    issue_textarea = next((t for t in parser.textareas if t.get("name") == "issue"), None)
    assert issue_textarea is not None, "Issue textarea not found"
    assert issue_textarea.get("maxlength") == "500", f"Expected maxlength 500 on issue, got {issue_textarea.get('maxlength')}"
    assert "required" in issue_textarea, "Expected required attribute on issue"

    print("All form validation tests passed!")

if __name__ == "__main__":
    test_form_validation()
