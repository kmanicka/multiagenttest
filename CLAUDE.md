# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**mathcli** is a command-line tool for basic mathematical operations, developed using a multi-agent workflow approach. This repository contains the implementation code.

**Your Role as Developer Agent:**
- Pick issues from the GitHub backlog
- Implement features according to acceptance criteria
- Write tests for implementations
- Create pull requests linking to issues
- Follow the development workflow documented in README.md

## Repository Structure

```
multiagenttest/
├── src/mathcli/           # Main package source
│   ├── __init__.py        # Package initialization, version info
│   ├── __main__.py        # CLI entry point (argparse-based)
│   └── operations.py      # Mathematical operations implementation
├── tests/                 # Test files (pytest)
├── .github/workflows/     # CI/CD (GitHub Actions)
├── pyproject.toml         # Package configuration
├── requirements.txt       # Runtime dependencies
└── requirements-dev.txt   # Dev dependencies (pytest, black, flake8)
```

## Development Setup

### Initial Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package in development mode
pip install -e .

# Install dev dependencies
pip install -r requirements-dev.txt
```

### Common Commands

**Run the CLI:**
```bash
mathcli --help
mathcli --version
mathcli <command> [args]  # e.g., mathcli add 5 10
```

**Testing:**
```bash
pytest                    # Run all tests
pytest tests/test_file.py # Run specific test file
pytest -v                 # Verbose output
pytest --cov=mathcli      # With coverage report
```

**Code Quality:**
```bash
black src/ tests/         # Format code
flake8 src/ tests/        # Lint code
```

**Git Workflow:**
```bash
# Pick an issue
gh issue view <number>
gh issue edit <number> --add-assignee @me

# Create feature branch
git checkout -b feature/issue-<number>-<description>

# After implementation
git add <files>
git commit -m "message with 'Closes #<number>'"
git push -u origin feature/issue-<number>-<description>
gh pr create --title "Title" --body "Description"
```

## Architecture

### CLI Design
- **Framework:** argparse (stdlib, no external dependencies)
- **Entry Point:** `src/mathcli/__main__.py:main()`
- **Command Structure:** Subparser pattern for extensibility
  - Each operation is a subcommand (add, subtract, multiply, divide)
  - Arguments passed as positional parameters

### Operations Module
- Location: `src/mathcli/operations.py`
- Each operation is a pure function
- Input validation and error handling at function level
- Return results or raise descriptive exceptions

### Testing Strategy
- Unit tests for all operations in `tests/`
- Test file naming: `test_<module>.py`
- Test function naming: `test_<function>_<scenario>()`
- Use pytest fixtures for common setup
- Aim for >80% code coverage

## Implementation Guidelines

### Adding New Operations

1. **Implement in operations.py:**
```python
def operation_name(a: float, b: float) -> float:
    """Brief description.

    Args:
        a: First operand
        b: Second operand

    Returns:
        Result of operation

    Raises:
        ValueError: If invalid input
    """
    # Implementation with validation
    return result
```

2. **Add CLI command in __main__.py:**
```python
# In main() function, after subparsers creation
cmd_parser = subparsers.add_parser('commandname', help='Help text')
cmd_parser.add_argument('a', type=float, help='First number')
cmd_parser.add_argument('b', type=float, help='Second number')

# In command routing section
if args.command == 'commandname':
    result = operations.operation_name(args.a, args.b)
    print(result)
```

3. **Write tests in tests/test_operations.py:**
```python
def test_operation_name_basic():
    assert operations.operation_name(x, y) == expected

def test_operation_name_edge_case():
    # Test edge cases, error conditions
```

### Code Style
- Follow PEP 8
- Use type hints for function signatures
- Include docstrings for all public functions
- Keep functions focused and simple
- Use descriptive variable names

### Error Handling
- Validate inputs early
- Raise descriptive exceptions (ValueError, TypeError)
- Catch and display user-friendly errors in CLI
- Don't suppress errors silently

### Commit Messages
```
<Action> <feature>: <brief description>

- Acceptance criterion 1 met
- Acceptance criterion 2 met
- Additional implementation details

Closes #<issue-number>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

## Multi-Agent Workflow

### Developer Agent (You)
1. Check open issues: `gh issue list --state open`
2. Pick next unassigned issue (follow dependencies)
3. Assign to yourself
4. Create feature branch
5. Implement according to acceptance criteria
6. Test locally
7. Commit and push
8. Create PR with detailed description
9. Link PR to issue with "Closes #N"

### Reviewer Agent (Separate)
- Reviews PRs for code quality
- Verifies acceptance criteria met
- Runs tests
- Approves or requests changes
- Merges when ready

### Current Status
- **Issue #2** (Project Setup): Completed - PR #9 awaiting review
- **Next Issues:** #3 (Addition), #4 (Subtraction), #5 (Multiplication), #6 (Division)
- **Dependencies:** Issues #3-6 require #2 to be merged first

## Important Notes

- **One issue at a time** - Complete and create PR before starting next
- **Follow dependencies** - Check issue descriptions for prerequisites
- **Match acceptance criteria** - Every checkbox should be addressed
- **Write tests** - Required for all operation implementations
- **Update documentation** - Keep README.md current with new features
- **Clean code** - Run black and flake8 before committing
- **CI must pass** - GitHub Actions will run on all PRs

## Package Information

- **Package Name:** mathcli
- **Version:** 0.1.0
- **Python Requirement:** >=3.8
- **Entry Point:** `mathcli` command
- **CI:** GitHub Actions (tests on Python 3.8, 3.9, 3.10, 3.11)
