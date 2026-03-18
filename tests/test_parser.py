from src.parser.lsof import LsofParser

def test_lsof_parse():
    line = "node      12345 user   22u  IPv4 0x123      0t0  TCP *:8080 (LISTEN)"
    entry = LsofParser.parse_line(line)
    assert entry is not None
    assert entry.process_name == "node"
    assert entry.pid == 12345
    assert entry.local_port == 8080
    assert entry.state == "LISTEN"
    assert LsofParser.parse_line("COMMAND PID USER") is None
