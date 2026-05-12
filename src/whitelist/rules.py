from typing import Set

class PortWhitelist:
    def __init__(self, allowed_ports: Set[int]):
        self.allowed = allowed_ports
        
    def is_allowed(self, port: int) -> bool:
        return port in self.allowed
