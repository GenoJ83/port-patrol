from src.reporter.table import TerminalReport
from src.patrol import PortPatrol
from src.core.models import SocketEntry

def test_reporter():
    sockets = [SocketEntry("TCP", "0.0.0.0", 80, "*", 0, "LISTEN", 1, "system")]
    txt = TerminalReport.render(PortPatrol(sockets).inspect())
    assert "PORT" in txt
    assert "HTTP" in txt
