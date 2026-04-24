from src.metrics.prom import to_prometheus

def test_metrics():
    m = to_prometheus({"listening_count": 5, "conflicts": []})
    assert "port_patrol_listening_sockets 5" in m
    assert "port_patrol_conflicts 0" in m
