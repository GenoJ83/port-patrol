from typing import List, Set

def find_next_available_port(occupied_ports: Set[int], start_port: int = 3000, end_port: int = 9000) -> int:
    for p in range(start_port, end_port + 1):
        if p not in occupied_ports:
            return p
    return -1
