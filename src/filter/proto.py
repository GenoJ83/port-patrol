from typing import List
from src.core.models import SocketEntry

def filter_by_protocol(sockets: List[SocketEntry], protocol: str = "TCP") -> List[SocketEntry]:
    return [s for s in sockets if s.protocol.upper() == protocol.upper()]
