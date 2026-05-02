from src.diff.compare import compare_listening_ports

def test_diff():
    opened, closed = compare_listening_ports({80, 443}, {80, 8080})
    assert opened == {8080} and closed == {443}
