import json
from src.export.json_out import export_json
from src.patrol import PortPatrol

def test_json_export():
    data = json.loads(export_json(PortPatrol().inspect()))
    assert "total_sockets" in data
    assert "conflicts" in data
