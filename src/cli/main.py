import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="portpatrol", description="Socket inspector and port conflict detector")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("--port", type=int, help="Filter by specific port number")
    p.add_argument("--kill", action="store_true", help="Terminate conflicting processes")
    p.add_argument("--dry-run", action="store_true", default=True, help="Dry run mode")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("portpatrol v0.1.0")
        return 0
    return 0
