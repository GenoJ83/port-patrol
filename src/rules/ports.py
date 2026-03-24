WELL_KNOWN_SERVICES = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt / Dev",
    27017: "MongoDB"
}

def identify_service(port: int) -> str:
    return WELL_KNOWN_SERVICES.get(port, "Unknown / Custom")

def is_privileged_port(port: int) -> bool:
    return 0 < port < 1024
