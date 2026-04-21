from src.finder.free_port import find_next_available_port

def test_free_port():
    occupied = {3000, 3001, 3002}
    assert find_next_available_port(occupied, start_port=3000) == 3003
