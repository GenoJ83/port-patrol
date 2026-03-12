from typing import List, Optional
from src.core.models import SocketEntry

class LsofParser:
    @staticmethod
    def parse_line(line: str) -> Optional[SocketEntry]:
        parts = line.strip().split()
        if len(parts) < 6 or parts[0] == "COMMAND":
            return None
        cmd = parts[0]
        try:
            pid = int(parts[1])
        except ValueError:
            pid = None
        proto = "TCP" if "TCP" in parts else ("UDP" if "UDP" in parts else "RAW")
        for token in parts:
            if ":" in token and not token.startswith("("):
                addr, port_str = token.rsplit(":", 1)
                try:
                    port = int(port_str)
                    return SocketEntry(protocol=proto, local_ip=addr, local_port=port, remote_ip="*", remote_port=0, state="LISTEN", pid=pid, process_name=cmd)
                except ValueError:
                    continue
        return None
