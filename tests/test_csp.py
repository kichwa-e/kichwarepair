def test_csp_policy():
    with open("kichwa_repair_with_blue_green_logo.html", "r") as f:
        content = f.read()
    assert "script-src 'self' https://cdn.tailwindcss.com;" in content
    assert "unsafe-inline" not in content.split("script-src")[1].split(";")[0]
