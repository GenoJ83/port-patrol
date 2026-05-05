from typing import List, Dict, Any
from src.core.models import SocketEntry

RISKY_PORTS = {21: "FTP (Unencrypted)", 23: "Telnet (Unencrypted)", 80: "HTTP (Cleartext)"}

def audit_security_risks(sockets: List[SocketEntry]) -> List[Dict[str, Any]]:
    risks = []
    for s in sockets:
        if s.state == "LISTEN" and s.local_port in RISKY_PORTS:
            risks.append({
                "port": s.local_port,
                "service": RISKY_PORTS[s.local_port],
                "pid": s.pid,
                "level": "WARNING"
            })
    return risks
