import sys


def run_cli():
    if len(sys.argv) < 2:
        print("Usage: python script.py [status|scan]")
        return
    cmd = sys.argv
    if cmd == "status":
        print("System: Secure")
    elif cmd == "scan":
        print("Scanning complete. No threats.")
    else:
        print("Unknown command")


if __name__ == "__main__":
    run_cli()
