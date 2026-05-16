from src.whitelist.rules import PortWhitelist

def test_whitelist():
    wl = PortWhitelist({80, 443, 8080})
    assert wl.is_allowed(443) is True
    assert wl.is_allowed(22) is False
