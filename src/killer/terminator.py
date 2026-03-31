from typing import List
import os
import signal

class ProcessTerminator:
    @staticmethod
    def terminate_pid(pid: int, dry_run: bool = True) -> bool:
        if dry_run:
            return True
        try:
            os.kill(pid, signal.SIGTERM)
            return True
        except OSError:
            return False
