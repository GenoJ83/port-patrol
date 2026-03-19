from typing import List, Dict
from src.core.models import SocketEntry, PortConflict

class ConflictAnalyzer:
    @staticmethod
    def detect_conflicts(sockets: List[SocketEntry]) -> List[PortConflict]:
        port_map: Dict[int, List[SocketEntry]] = {}
        for s in sockets:
            if s.state == "LISTEN":
                port_map.setdefault(s.local_port, []).append(s)
        conflicts = []
        for port, entries in port_map.items():
            unique_pids = list(set(e.pid for e in entries if e.pid is not None))
            if len(unique_pids) > 1:
                names = list(set(e.process_name for e in entries if e.process_name))
                conflicts.append(PortConflict(port=port, conflicting_pids=unique_pids, process_names=names))
        return sorted(conflicts, key=lambda c: c.port)
