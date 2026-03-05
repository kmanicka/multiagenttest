"""Main entry point for the mathcli command-line tool."""

import argparse
import sys
from mathcli import __version__


def main():
    """Main function for the mathcli CLI."""
    parser = argparse.ArgumentParser(
        description="A command-line tool for mathematical operations", prog="mathcli"
    )
    parser.add_argument("--version", action="version", version=f"mathcli {__version__}")

    subparsers = parser.add_subparsers(  # noqa: F841
        dest="command", help="Available commands"
    )

    # Placeholder for future commands
    # Commands will be added in subsequent issues:
    # - add: Addition operation
    # - subtract: Subtraction operation
    # - multiply: Multiplication operation
    # - divide: Division operation

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Command routing will be implemented when operations are added


if __name__ == "__main__":
    main()
