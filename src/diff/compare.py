from typing import Set, Tuple

def compare_listening_ports(prev_ports: Set[int], curr_ports: Set[int]) -> Tuple[Set[int], Set[int]]:
    opened = curr_ports - prev_ports
    closed = prev_ports - curr_ports
    return opened, closed
