from src.patrol import PortPatrol
from src.core.models import SocketEntry
from src.reporter.table import TerminalReport
from src.export.json_out import export_json

def test_full_port_patrol_workflow():
    s1 = SocketEntry("TCP", "0.0.0.0", 3000, "*", 0, "LISTEN", 101, "dev-server")
    s2 = SocketEntry("TCP", "0.0.0.0", 3000, "*", 0, "LISTEN", 102, "docker-proxy")
    patrol = PortPatrol([s1, s2])
    res = patrol.inspect()
    assert res["has_conflicts"] is True
    table = TerminalReport.render(res)
    assert "Conflicting ports" in table
    json_data = export_json(res)
    assert "docker-proxy" in json_data
