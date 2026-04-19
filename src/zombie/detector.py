from typing import List
from src.core.models import SocketEntry

ZOMBIE_STATES = ["CLOSE_WAIT", "FIN_WAIT_2", "TIME_WAIT"]

def find_zombies(sockets: List[SocketEntry]) -> List[SocketEntry]:
    return [s for s in sockets if s.state.upper() in ZOMBIE_STATES]
