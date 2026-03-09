from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SocketEntry:
    protocol: str
    local_ip: str
    local_port: int
    remote_ip: str
    remote_port: int
    state: str
    pid: Optional[int]
    process_name: Optional[str]
    
@dataclass
class PortConflict:
    port: int
    conflicting_pids: List[int]
    process_names: List[str]
