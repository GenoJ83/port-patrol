from src.speed.probe import estimate_connect_latency_ms

def test_speed():
    assert estimate_connect_latency_ms() > 0
