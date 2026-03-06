# Contributing to mathcli

Thank you for your interest in contributing to mathcli! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, professional, and inclusive in all interactions.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account

### Setting Up Your Environment

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/multiagenttest.git
   cd multiagenttest
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode:**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

4. **Verify installation:**
   ```bash
   mathcli --version
   pytest
   ```

## Development Workflow

### 1. Pick an Issue

- Check [open issues](https://github.com/kmanicka/multiagenttest/issues)
- Comment on the issue to claim it
- Get assigned by a maintainer

### 2. Create a Branch

```bash
git checkout -b feature/issue-NUMBER-description
# Example: git checkout -b feature/issue-10-add-power-operation
```

### 3. Make Your Changes

- Follow the code style guidelines (see below)
- Write tests for new functionality
- Update documentation as needed
- Keep commits focused and atomic

### 4. Test Your Changes

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_operations.py

# Check coverage
pytest --cov=mathcli --cov-report=term

# Must meet coverage threshold
pytest --cov=mathcli --cov-fail-under=80

# Lint code
flake8 src/ tests/

# Format code
black src/ tests/
```

### 5. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add <files>
git commit -m "Add power operation

- Implement pow() function in operations.py
- Add CLI integration in __main__.py
- Add comprehensive tests
- Update documentation

Closes #10

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

### 6. Push and Create Pull Request

```bash
git push -u origin feature/issue-NUMBER-description
```

Then create a PR on GitHub with:
- Clear title describing the change
- Description of changes made
- Link to issue (`Closes #NUMBER`)
- Screenshots/examples if applicable

## Code Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting (max line length: 88)
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use type hints for function signatures
- Write docstrings for all public functions

### Docstring Format

```python
def operation_name(arg1: float, arg2: float) -> float:
    """Brief one-line description.

    Longer description if needed, explaining the operation
    in more detail.

    Args:
        arg1: Description of first argument
        arg2: Description of second argument

    Returns:
        Description of return value

    Raises:
        ValueError: When this exception is raised
        ZeroDivisionError: When this exception is raised

    Examples:
        >>> operation_name(5, 10)
        15.0
    """
    # Implementation
```

### Testing

- Write tests for all new functionality
- Aim for >80% code coverage (90%+ preferred)
- Test both success and failure cases
- Use descriptive test names: `test_<function>_<scenario>()`
- Group related tests in test classes

Example test structure:
```python
class TestNewOperation:
    """Test cases for the new operation."""

    def test_new_operation_basic(self):
        """Test basic functionality."""
        assert new_operation(5, 10) == expected

    def test_new_operation_edge_case(self):
        """Test edge case."""
        assert new_operation(0, 0) == expected

    def test_new_operation_error(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            new_operation(invalid_input)
```

## Project Structure

```
multiagenttest/
├── src/mathcli/           # Source code
│   ├── __init__.py        # Package init, version
│   ├── __main__.py        # CLI entry point
│   └── operations.py      # Math operations
├── tests/                 # Test files
│   ├── test_operations.py # Unit tests
│   └── test_cli.py        # CLI integration tests
├── .github/workflows/     # CI/CD configuration
├── docs/                  # Additional documentation
├── examples/              # Usage examples
├── pyproject.toml         # Package configuration
├── requirements.txt       # Runtime dependencies
└── requirements-dev.txt   # Development dependencies
```

## Adding New Operations

To add a new mathematical operation:

### 1. Implement function in `src/mathcli/operations.py`

```python
def power(*numbers: float) -> float:
    """Calculate power of numbers from left to right.

    Raises the first number to the power of subsequent numbers.
    For example: power(2, 3, 2) = (2^3)^2 = 64

    Args:
        *numbers: Variable number of numeric arguments (minimum 2)

    Returns:
        float: The result of the power operation

    Raises:
        ValueError: If fewer than 2 numbers provided

    Examples:
        >>> power(2, 3)
        8.0
        >>> power(2, 3, 2)
        64.0
    """
    if len(numbers) < 2:
        raise ValueError("power requires at least 2 numbers")

    result = numbers[0]
    for num in numbers[1:]:
        result = result ** num
    return result
```

### 2. Add CLI command in `src/mathcli/__main__.py`

Add subparser:
```python
# Power command
power_parser = subparsers.add_parser(
    "power", help="Calculate power from left to right"
)
power_parser.add_argument(
    "numbers",
    nargs="+",
    type=float,
    help="Numbers for power calculation (first ^ second ^ third...)",
)
```

Add command handler:
```python
elif args.command == "power":
    try:
        if len(args.numbers) < 2:
            print("Error: power requires at least 2 numbers", file=sys.stderr)
            sys.exit(1)
        result = operations.power(*args.numbers)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```

### 3. Write tests in `tests/test_operations.py`

```python
class TestPower:
    """Test cases for the power operation."""

    def test_power_two_numbers(self):
        """Test raising to a power."""
        assert power(2, 3) == 8.0

    def test_power_multiple_numbers(self):
        """Test multiple power operations."""
        assert power(2, 3, 2) == 64.0

    def test_power_insufficient_arguments(self):
        """Test that power requires at least 2 numbers."""
        with pytest.raises(ValueError, match="power requires at least 2 numbers"):
            power(5)
```

### 4. Add CLI tests in `tests/test_cli.py`

```python
class TestCLIPower:
    """Test CLI power command."""

    def test_power_two_numbers(self):
        """Test power via CLI."""
        result = run_cli("power", "2", "3")
        if result.returncode == 0:
            assert "8" in result.stdout.strip()

    def test_power_direct(self):
        """Test power command directly."""
        return_code, stdout, stderr = run_cli_direct("power", "2", "3")
        assert return_code == 0
        assert "8" in stdout
```

### 5. Update documentation

- Add to README.md usage section
- Update help text to be descriptive
- Add examples to show usage

## Pull Request Process

### 1. Ensure all checks pass

Before submitting your PR:

- ✅ All tests pass (`pytest`)
- ✅ Code coverage >80% (`pytest --cov=mathcli --cov-fail-under=80`)
- ✅ No linting errors (`flake8 src/ tests/`)
- ✅ Code is formatted with black (`black --check src/ tests/`)

### 2. Update documentation

If your changes affect users:
- Update README.md with new features/usage
- Update docstrings for modified functions
- Add examples if applicable

### 3. Get review

- Wait for maintainer review
- Address feedback promptly
- Make requested changes
- Be responsive to questions

### 4. Merge

- Maintainer will merge when approved
- Delete your branch after merge
- Close any related issues

## Testing Guidelines

### Unit Tests

- Test one function at a time
- Mock external dependencies (if any)
- Cover edge cases:
  - Empty/null inputs
  - Boundary values
  - Invalid inputs
  - Large/small numbers
- Test error paths

### Integration Tests

- Test end-to-end workflows
- Verify CLI commands work correctly
- Check error messages and exit codes
- Test with real subprocess calls

### Coverage

Run coverage report to see what's missing:
```bash
pytest --cov=mathcli --cov-report=html
open htmlcov/index.html
```

Aim for:
- >90% overall coverage
- 100% for business logic (operations.py)
- >80% for CLI code (__main__.py)

## Release Process

(For maintainers)

1. Update version in `src/mathcli/__init__.py`
2. Update CHANGELOG.md with release notes
3. Create git tag: `git tag v0.x.0`
4. Push tag: `git push --tags`
5. GitHub Actions will run tests and checks
6. Create GitHub release with notes

## Common Issues

### Tests failing locally but pass in CI

- Check Python version matches CI
- Ensure clean virtual environment
- Check for local configuration files

### Coverage below threshold

- Run `pytest --cov=mathcli --cov-report=html`
- Open htmlcov/index.html to see uncovered lines
- Add tests for missing coverage

### Linting errors

- Run `black src/ tests/` to auto-format
- Run `flake8 src/ tests/` to see specific issues
- Fix any remaining issues manually

## Getting Help

- **Questions about an issue**: Comment on the issue
- **General questions**: Open a new issue with "Question:" prefix
- **Bugs**: Open a new issue with steps to reproduce
- **Feature requests**: Open a new issue describing the feature

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgments

mathcli is developed using a multi-agent workflow. Thank you to all contributors!
