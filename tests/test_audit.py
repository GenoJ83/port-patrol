from src.audit.risks import audit_security_risks
from src.core.models import SocketEntry

def test_risks():
    s = SocketEntry("TCP", "0.0.0.0", 23, "*", 0, "LISTEN", 99, "telnetd")
    risks = audit_security_risks([s])
    assert len(risks) == 1
    assert "Telnet" in risks[0]["service"]
