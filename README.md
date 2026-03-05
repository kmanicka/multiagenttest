# mathcli - Mathematical Operations CLI Tool

A command-line tool for performing basic mathematical operations.

## Description

`mathcli` is a simple, easy-to-use command-line interface for basic mathematical operations including addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Simple and intuitive command-line interface
- Input validation and error handling

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/kmanicka/multiagenttest.git
cd multiagenttest
```

2. Install in development mode:
```bash
pip install -e .
```

### Requirements

- Python 3.8 or higher

## Usage

After installation, the `mathcli` command will be available in your terminal.

### View Help
```bash
mathcli --help
```

### Check Version
```bash
mathcli --version
```

### Basic Operations (Coming Soon)

The following commands will be available in upcoming releases:

```bash
# Addition
mathcli add 5 10

# Subtraction
mathcli subtract 20 8

# Multiplication
mathcli multiply 6 7

# Division
mathcli divide 100 5
```

## Development Setup

### Prerequisites

- Python 3.8+
- pip

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/kmanicka/multiagenttest.git
cd multiagenttest
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Running Tests

```bash
pytest
```

### Running Tests with Coverage

```bash
pytest --cov=mathcli
```

### Code Formatting

```bash
black src/ tests/
```

### Linting

```bash
flake8 src/ tests/
```

## Project Structure

```
multiagenttest/
├── src/
│   └── mathcli/
│       ├── __init__.py        # Package initialization
│       ├── __main__.py        # CLI entry point
│       └── operations.py      # Mathematical operations
├── tests/
│   └── __init__.py            # Test package
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD configuration
├── pyproject.toml             # Project configuration
├── requirements.txt           # Runtime dependencies
├── requirements-dev.txt       # Development dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Contributing

This project is developed using a multi-agent workflow. For contribution guidelines, please see the project documentation.

## License

To be determined

## Authors

Multi-Agent Development Team

## Project Status

This project is currently in active development. Features are being added incrementally through a multi-agent development process.
