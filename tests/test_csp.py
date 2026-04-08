import unittest
import re

class TestCSP(unittest.TestCase):
    def test_csp_presence(self):
        with open('kichwa_repair_with_blue_green_logo.html', 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Find meta tags
        meta_tags = re.findall(r'<meta\s+[^>]*>', html_content, re.IGNORECASE)
        csp_content = None

        for tag in meta_tags:
            if 'http-equiv="Content-Security-Policy"' in tag or "http-equiv='Content-Security-Policy'" in tag:
                # Extract content attribute, handling double and single quotes correctly
                match_double = re.search(r'content="(.*?)"', tag, re.IGNORECASE)
                match_single = re.search(r"content='(.*?)'", tag, re.IGNORECASE)

                if match_double:
                    csp_content = match_double.group(1)
                elif match_single:
                    csp_content = match_single.group(1)

                if csp_content:
                    break

        self.assertIsNotNone(csp_content, "CSP meta tag missing or content attribute not found")

        # Verify directives
        self.assertIn("default-src 'self'", csp_content)
        self.assertIn("script-src 'self'", csp_content)
        self.assertIn("https://cdn.tailwindcss.com", csp_content)
        self.assertIn("frame-src 'self'", csp_content)
        self.assertIn("https://www.google.com", csp_content)

if __name__ == '__main__':
    unittest.main()
