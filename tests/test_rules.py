from src.rules.ports import identify_service, is_privileged_port

def test_port_rules():
    assert identify_service(5432) == "PostgreSQL"
    assert identify_service(9999) == "Unknown / Custom"
    assert is_privileged_port(80) is True
    assert is_privileged_port(8080) is False
