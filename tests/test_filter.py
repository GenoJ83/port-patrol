from src.filter.proto import filter_by_protocol
from src.core.models import SocketEntry

def test_protocol_filter():
    s1 = SocketEntry("TCP", "0", 1, "*", 0, "LISTEN", 1, "a")
    s2 = SocketEntry("UDP", "0", 2, "*", 0, "LISTEN", 2, "b")
    assert len(filter_by_protocol([s1, s2], "TCP")) == 1
