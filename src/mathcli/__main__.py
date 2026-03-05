"""Main entry point for the mathcli command-line tool."""

import argparse
import sys
from mathcli import __version__
from mathcli import operations


def main():
    """Main function for the mathcli CLI."""
    parser = argparse.ArgumentParser(
        description="A command-line tool for mathematical operations", prog="mathcli"
    )
    parser.add_argument("--version", action="version", version=f"mathcli {__version__}")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add two or more numbers")
    add_parser.add_argument(
        "numbers", nargs="+", type=float, help="Numbers to add (space-separated)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Command routing
    if args.command == "add":
        try:
            if len(args.numbers) < 2:
                print("Error: add requires at least 2 numbers", file=sys.stderr)
                sys.exit(1)
            result = operations.add(*args.numbers)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
