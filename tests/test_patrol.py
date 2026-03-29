from src.patrol import PortPatrol
from src.core.models import SocketEntry

def test_patrol_inspection():
    sockets = [SocketEntry("TCP", "127.0.0.1", 6379, "*", 0, "LISTEN", 555, "redis-server")]
    patrol = PortPatrol(sockets)
    res = patrol.inspect()
    assert res["listening_count"] == 1
    assert res["has_conflicts"] is False
    assert res["ports"][0]["service"] == "Redis"
