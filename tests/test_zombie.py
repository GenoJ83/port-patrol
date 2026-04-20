from src.zombie.detector import find_zombies
from src.core.models import SocketEntry

def test_zombie_detection():
    s1 = SocketEntry("TCP", "1.1.1.1", 1000, "2.2.2.2", 80, "CLOSE_WAIT", 10, "proc")
    s2 = SocketEntry("TCP", "1.1.1.1", 1001, "2.2.2.2", 80, "ESTABLISHED", 10, "proc")
    z = find_zombies([s1, s2])
    assert len(z) == 1 and z[0].state == "CLOSE_WAIT"
