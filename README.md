# mathcli

A simple, fast, and reliable command-line calculator for basic mathematical operations.

[![CI](https://github.com/kmanicka/multiagenttest/actions/workflows/ci.yml/badge.svg)](https://github.com/kmanicka/multiagenttest/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Features

- ✅ **Four basic operations**: Addition, Subtraction, Multiplication, Division
- ✅ **Multiple numbers**: Operate on 2 or more numbers at once
- ✅ **Float support**: Works with integers and decimals
- ✅ **Error handling**: Clear error messages for invalid input
- ✅ **Zero dependencies**: Only uses Python standard library
- ✅ **Cross-platform**: Works on Linux, macOS, and Windows
- ✅ **Well-tested**: >80% code coverage with comprehensive tests

## Installation

### From Source

```bash
git clone https://github.com/kmanicka/multiagenttest.git
cd multiagenttest
pip install -e .
```

### Requirements

- Python 3.8 or higher

## Quick Start

```bash
# Addition
mathcli add 5 10 15
# Output: 30.0

# Subtraction
mathcli subtract 100 25 10
# Output: 65.0

# Multiplication
mathcli multiply 2 3 4
# Output: 24.0

# Division
mathcli divide 100 2 5
# Output: 10.0
```

## Usage

### Basic Operations

**Addition** - Sum all numbers:
```bash
mathcli add <number1> <number2> [number3 ...]

# Examples
mathcli add 5 10          # 15.0
mathcli add 1.5 2.5 3.0   # 7.0
mathcli add -5 10 -3      # 2.0
```

**Subtraction** - Subtract from left to right:
```bash
mathcli subtract <number1> <number2> [number3 ...]

# Examples
mathcli subtract 10 3     # 7.0
mathcli subtract 100 25 10 5  # 60.0
mathcli subtract 5 10     # -5.0
```

**Multiplication** - Multiply all numbers:
```bash
mathcli multiply <number1> <number2> [number3 ...]

# Examples
mathcli multiply 5 4      # 20.0
mathcli multiply 2 3 4    # 24.0
mathcli multiply 2.5 4    # 10.0
```

**Division** - Divide from left to right:
```bash
mathcli divide <number1> <number2> [number3 ...]

# Examples
mathcli divide 20 4       # 5.0
mathcli divide 100 2 5    # 10.0
mathcli divide 10 3       # 3.333333333333333
```

### Command-Line Options

```bash
# Show version
mathcli --version

# Show help
mathcli --help

# Show help for specific command
mathcli add --help
```

## Common Use Cases

### Calculating Totals
```bash
# Sum expenses
mathcli add 12.50 8.75 15.00 22.30
# Output: 58.55

# Calculate tax (price * (1 + tax rate))
mathcli multiply 100 1.08
# Output: 108.0
```

### Financial Calculations
```bash
# Split bill among friends
mathcli divide 125.50 4
# Output: 31.375

# Calculate percentage
mathcli multiply 250 0.15  # 15% of 250
# Output: 37.5
```

### Chain Calculations
```bash
# Use command substitution for complex calculations
# Calculate (10 + 5) * 2
mathcli multiply $(mathcli add 10 5) 2
# Output: 30.0
```

## Error Handling

mathcli provides clear error messages:

```bash
# Division by zero
mathcli divide 10 0
# Error: Cannot divide by zero

# Insufficient arguments
mathcli add 5
# Error: add requires at least 2 numbers

# Invalid input
mathcli add 5 abc
# Error: argument numbers: invalid float value: 'abc'
```

**Exit codes:**
- `0` - Success
- `1` - Error (invalid input, division by zero, etc.)

## Troubleshooting

**Command not found:**
- Ensure mathcli is installed: `pip list | grep mathcli`
- Verify your PATH includes pip's bin directory
- Try reinstalling: `pip install --force-reinstall -e .`

**Import errors:**
- Check Python version: `python --version` (must be 3.8+)
- Reinstall dependencies: `pip install -r requirements-dev.txt`

**Unexpected results:**
- Check operation order (subtract/divide go left-to-right)
- Verify number format (use `.` for decimals, not `,`)
- Remember: `subtract(100, 25, 10)` = 100 - 25 - 10 = 65

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed development setup and guidelines.

### Quick Development Setup

```bash
# Clone and setup
git clone https://github.com/kmanicka/multiagenttest.git
cd multiagenttest
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_operations.py
pytest tests/test_cli.py

# Run with coverage
pytest --cov=mathcli --cov-report=term-missing

# Run with coverage threshold check
pytest --cov=mathcli --cov-fail-under=80
```

### Code Quality

```bash
# Format code
black src/ tests/

# Check formatting
black --check src/ tests/

# Lint code
flake8 src/ tests/
```

## Project Structure

```
multiagenttest/
├── src/mathcli/           # Main package source
│   ├── __init__.py        # Package initialization, version info
│   ├── __main__.py        # CLI entry point (argparse-based)
│   └── operations.py      # Mathematical operations implementation
├── tests/                 # Test files (pytest)
│   ├── test_operations.py # Unit tests for operations
│   └── test_cli.py        # CLI integration tests
├── .github/workflows/     # CI/CD (GitHub Actions)
│   └── ci.yml             # Multi-OS, multi-Python version testing
├── docs/                  # Additional documentation
├── examples/              # Usage examples
├── pyproject.toml         # Package configuration
├── requirements.txt       # Runtime dependencies (none)
└── requirements-dev.txt   # Dev dependencies (pytest, black, flake8)
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:

- Development setup
- Code style guidelines
- Testing requirements
- Pull request process

## Architecture

For details on the system design and architecture, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## License

[MIT License](LICENSE)

## Authors

- Development managed through multi-agent workflow
- See [contributors](https://github.com/kmanicka/multiagenttest/graphs/contributors) on GitHub

## Links

- **GitHub Repository**: https://github.com/kmanicka/multiagenttest
- **Issues**: https://github.com/kmanicka/multiagenttest/issues
- **CI/CD**: https://github.com/kmanicka/multiagenttest/actions

## Changelog

### v0.1.0 (Initial Release)

- ✅ Basic arithmetic operations (add, subtract, multiply, divide)
- ✅ Support for multiple arguments
- ✅ Comprehensive error handling with clear messages
- ✅ Full test coverage (>90%)
- ✅ Cross-platform support (Linux, macOS, Windows)
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Complete documentation and examples
