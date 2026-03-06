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

    # Subtract command
    subtract_parser = subparsers.add_parser(
        "subtract", help="Subtract numbers from left to right"
    )
    subtract_parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Numbers to subtract (first - second - third...)",
    )

    # Multiply command
    multiply_parser = subparsers.add_parser(
        "multiply", help="Multiply two or more numbers"
    )
    multiply_parser.add_argument(
        "numbers", nargs="+", type=float, help="Numbers to multiply (space-separated)"
    )

    # Divide command
    divide_parser = subparsers.add_parser(
        "divide", help="Divide numbers from left to right"
    )
    divide_parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Numbers to divide (first / second / third...)",
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
    elif args.command == "subtract":
        try:
            if len(args.numbers) < 2:
                print("Error: subtract requires at least 2 numbers", file=sys.stderr)
                sys.exit(1)
            result = operations.subtract(*args.numbers)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "multiply":
        try:
            if len(args.numbers) < 2:
                print("Error: multiply requires at least 2 numbers", file=sys.stderr)
                sys.exit(1)
            result = operations.multiply(*args.numbers)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "divide":
        try:
            if len(args.numbers) < 2:
                print("Error: divide requires at least 2 numbers", file=sys.stderr)
                sys.exit(1)
            result = operations.divide(*args.numbers)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except ZeroDivisionError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
