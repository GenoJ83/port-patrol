from src.killer.terminator import ProcessTerminator

def test_terminator():
    assert ProcessTerminator.terminate_pid(99999, dry_run=True) is True
