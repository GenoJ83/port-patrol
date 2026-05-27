# port-patrol

Local network socket mapper, port conflict detector, listening process inspector, and zombie connection cleaner.

[![CI](https://github.com/GenoJ83/port-patrol/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/port-patrol/actions)

## Features
- **Port Conflict Detector**: Instantly flags multiple processes contending for the same port
- **Socket Parser**: Parses listening TCP/UDP tables with process name and PID mapping
- **Zombie Connection Cleaner**: Detects sockets stuck in `CLOSE_WAIT` or `TIME_WAIT`
- **Security Audit**: Identifies cleartext and legacy protocols (Telnet, FTP, unencrypted HTTP)

## Quick Start
```python
from src.patrol import PortPatrol
from src.parser.lsof import LsofParser

line = "node 1234 user 20u IPv4 0x1 0t0 TCP *:3000 (LISTEN)"
socket = LsofParser.parse_line(line)
patrol = PortPatrol([socket])
audit = patrol.inspect()
print(audit["listening_count"])  # 1
```
