from typing import List, Dict, Any
from src.core.models import SocketEntry
from src.analyzer.conflict import ConflictAnalyzer
from src.rules.ports import identify_service

class PortPatrol:
    def __init__(self, sockets: List[SocketEntry] = None):
        self.sockets = sockets or []
        
    def inspect(self) -> Dict[str, Any]:
        listening = [s for s in self.sockets if s.state == "LISTEN"]
        conflicts = ConflictAnalyzer.detect_conflicts(self.sockets)
        summary_ports = []
        for s in listening:
            summary_ports.append({
                "port": s.local_port,
                "service": identify_service(s.local_port),
                "process": s.process_name,
                "pid": s.pid
            })
        return {
            "total_sockets": len(self.sockets),
            "listening_count": len(listening),
            "conflicts": conflicts,
            "has_conflicts": len(conflicts) > 0,
            "ports": summary_ports
        }
