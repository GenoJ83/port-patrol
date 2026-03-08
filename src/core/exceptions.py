class PortPatrolError(Exception):
    """Base exception."""

class PortInUseError(PortPatrolError):
    """Raised when desired port is already bound."""

class ProcessKillError(PortPatrolError):
    """Raised when terminating a conflicting process fails."""
