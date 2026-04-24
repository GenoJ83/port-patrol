from typing import Dict, Any

def to_prometheus(audit: Dict[str, Any]) -> str:
    return f"port_patrol_listening_sockets {audit['listening_count']}\nport_patrol_conflicts {len(audit['conflicts'])}"
