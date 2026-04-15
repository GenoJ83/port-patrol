from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["--port", "8080", "--kill"])
    assert opts.port == 8080
    assert opts.kill is True
    assert main(["--version"]) == 0
