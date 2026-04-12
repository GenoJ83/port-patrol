import json
from typing import Dict, Any

def export_json(audit: Dict[str, Any]) -> str:
    cleaned = dict(audit)
    cleaned["conflicts"] = [
        {"port": c.port, "pids": c.conflicting_pids, "processes": c.process_names}
        for c in audit["conflicts"]
    ]
    return json.dumps(cleaned, indent=2)
