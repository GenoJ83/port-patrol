from typing import Dict, Any

class TerminalReport:
    @staticmethod
    def render(audit: Dict[str, Any]) -> str:
        h1 = "PORT"
        h2 = "SERVICE"
        h3 = "PROCESS"
        h4 = "PID"
        lines = [f"{h1:<8} | {h2:<18} | {h3:<15} | {h4}"]
        lines.append("-" * 55)
        for p in audit["ports"]:
            lines.append(f"{p['port']:<8} | {p['service']:<18} | {str(p['process']):<15} | {p['pid']}")
        if audit["has_conflicts"]:
            lines.append("\n[!] WARNING: Conflicting ports detected:")
            for c in audit["conflicts"]:
                lines.append(f"  • Port {c.port} occupied by PIDs {c.conflicting_pids}")
        return "\n".join(lines)
