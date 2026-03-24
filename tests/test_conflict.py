from src.analyzer.conflict import ConflictAnalyzer
from src.core.models import SocketEntry

def test_conflict_detection():
    s1 = SocketEntry("TCP", "0.0.0.0", 3000, "*", 0, "LISTEN", 100, "node")
    s2 = SocketEntry("TCP", "0.0.0.0", 3000, "*", 0, "LISTEN", 200, "python")
    s3 = SocketEntry("TCP", "0.0.0.0", 8080, "*", 0, "LISTEN", 300, "nginx")
    conflicts = ConflictAnalyzer.detect_conflicts([s1, s2, s3])
    assert len(conflicts) == 1
    assert conflicts[0].port == 3000
    assert set(conflicts[0].conflicting_pids) == {100, 200}
