# mathcli Architecture

## Overview

mathcli is a simple CLI calculator built with Python's standard library. It follows a modular architecture separating concerns between CLI handling, business logic, and testing.

## Architecture Diagram

```
┌─────────────────────────────────────────┐
│           User Interface                │
│         (Command Line)                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      CLI Layer (__main__.py)            │
│  - Argument parsing (argparse)          │
│  - Command routing                      │
│  - Error formatting                     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│   Business Logic (operations.py)        │
│  - Mathematical operations              │
│  - Input validation                     │
│  - Exception raising                    │
└─────────────────────────────────────────┘
```

## Components

### 1. CLI Layer (`__main__.py`)

**Responsibility:** Handle user interaction

- Parse command-line arguments using argparse
- Route commands to appropriate operations
- Format and display output
- Handle exceptions and show user-friendly errors
- Set exit codes (0 for success, 1 for errors)

**Design Pattern:** Command pattern with subparsers

**Key Functions:**
- `main()` - Entry point for CLI application
- Argument parsing with `argparse.ArgumentParser`
- Subparser creation for each operation
- Exception handling and error formatting

### 2. Operations Module (`operations.py`)

**Responsibility:** Implement business logic

- Pure functions for mathematical operations
- Accept typed inputs, return typed outputs
- Validate inputs and raise exceptions
- No I/O or side effects

**Design Pattern:** Functional programming

**Functions:**
- `add(*numbers)` - Sum all numbers
- `subtract(*numbers)` - Subtract left-to-right
- `multiply(*numbers)` - Multiply all numbers
- `divide(*numbers)` - Divide left-to-right with zero-division checks

### 3. Package Init (`__init__.py`)

**Responsibility:** Package metadata

- Define version number
- Export public API
- Package-level documentation

## Design Decisions

### Why argparse?

- **Standard library**: No external dependencies
- **Well-documented**: Extensive Python documentation
- **Mature**: Battle-tested, stable API
- **Subcommand support**: Natural fit for multi-operation CLI
- **Automatic help**: Generates --help output automatically
- **Type conversion**: Built-in type validation

### Why separate operations module?

- **Separation of concerns**: CLI handling vs business logic
- **Easier to test**: No CLI mocking needed for unit tests
- **Reusable**: Can be imported as a library
- **Clear boundaries**: Single responsibility principle
- **Maintainable**: Changes to CLI don't affect logic and vice versa

### Why type hints?

- **Better IDE support**: Autocomplete and type checking
- **Self-documenting**: Function signatures show expected types
- **Easier to maintain**: Catch type errors early
- **Professional**: Industry best practice

### Why pytest?

- **Industry standard**: Most widely used Python testing framework
- **Rich plugin ecosystem**: pytest-cov, pytest-xdist, etc.
- **Clear syntax**: Readable test code
- **Good error messages**: Helpful failure output
- **Fixtures**: Powerful setup/teardown mechanism

## Data Flow

```
User Input (e.g., "mathcli add 5 10")
    ↓
argparse parses arguments
    ↓
Creates args object: {command: 'add', numbers: [5.0, 10.0]}
    ↓
Command router selects operation
    ↓
Calls operations.add(5.0, 10.0)
    ↓
Function validates and computes result → 15.0
    ↓
Return to CLI layer
    ↓
Print result to stdout → "15.0"
    ↓
Exit with code 0
```

## Error Handling Strategy

### Operation Level

- Raise descriptive exceptions (`ValueError`, `ZeroDivisionError`)
- Include error context in message
- Don't catch exceptions (let caller handle)
- Validate inputs before processing

Example:
```python
if len(numbers) < 2:
    raise ValueError("add requires at least 2 numbers")
```

### CLI Level

- Catch operation exceptions
- Format user-friendly error messages
- Write errors to stderr (not stdout)
- Exit with code 1 on errors

Example:
```python
try:
    result = operations.divide(*args.numbers)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
```

### Error Flow Example

```
User: mathcli divide 10 0
  ↓
CLI parses: command='divide', numbers=[10.0, 0.0]
  ↓
Calls: operations.divide(10.0, 0.0)
  ↓
Function checks: numbers[1] == 0
  ↓
Raises: ZeroDivisionError("Cannot divide by zero")
  ↓
CLI catches exception
  ↓
Prints to stderr: "Error: Cannot divide by zero"
  ↓
Exits with code 1
```

## Extension Points

### Adding New Operations

1. **Add function to `operations.py`**
   - Implement pure function with type hints
   - Add input validation
   - Add docstring with examples
   - Raise appropriate exceptions

2. **Add subparser to `__main__.py`**
   - Create new subparser for command
   - Define arguments (usually `numbers` with `nargs='+'`)
   - Add help text

3. **Add command handler to `__main__.py`**
   - Add elif branch in command routing
   - Validate minimum arguments
   - Call operation function
   - Handle exceptions

4. **Add tests to `tests/`**
   - Unit tests in `test_operations.py`
   - CLI tests in `test_cli.py`
   - Cover edge cases and errors

### Adding New Features

- **Input validation**: Extend `operations.py` functions
- **Output formatting**: Modify `__main__.py` print statements
- **New commands**: Add subparsers and handlers
- **Configuration**: Add command-line arguments
- **Logging**: Import logging module and add handlers

## Testing Strategy

### Unit Tests (`tests/test_operations.py`)

**Purpose:** Test business logic in isolation

- Test each operation independently
- Mock-free (pure functions don't need mocking)
- Cover edge cases: zero, negative, floats, large numbers
- Test error conditions
- Fast execution (<100ms for all unit tests)

**Structure:**
```python
class TestAdd:
    def test_add_two_numbers(self):
        assert add(5, 10) == 15

    def test_add_insufficient_arguments(self):
        with pytest.raises(ValueError):
            add(5)
```

### Integration Tests (`tests/test_cli.py`)

**Purpose:** Test complete CLI workflows

- Test via subprocess (real command execution)
- Test via direct function calls (for coverage)
- Verify output format and exit codes
- Test error messages
- Slower but comprehensive

**Approaches:**
1. Subprocess tests - Real CLI execution
2. Direct tests - Import main() and mock sys.argv

### Coverage Goals

- **Overall:** >80% (currently >90%)
- **operations.py:** 100% (business logic must be fully tested)
- **__main__.py:** >85% (CLI code, some branches hard to test)
- **Focus:** Meaningful tests, not just coverage numbers

## Dependencies

### Runtime

**None** - Pure Python 3.8+ stdlib only

Benefits:
- No dependency conflicts
- Fast installation
- Minimal security surface
- Easy deployment

### Development

- **pytest** - Testing framework
- **pytest-cov** - Coverage reporting
- **black** - Code formatting
- **flake8** - Linting and style checking

### CI/CD

- **GitHub Actions** - Automated testing and deployment
- **Multi-OS testing** - Ubuntu, macOS, Windows
- **Multi-Python testing** - Python 3.8, 3.9, 3.10, 3.11, 3.12

## Security Considerations

### Input Validation

- argparse handles type conversion securely
- Float conversion prevents injection attacks
- No eval() or exec() usage
- No shell command execution with user input

### Error Messages

- Don't leak sensitive information
- Don't show stack traces to end users
- Log errors appropriately (not implemented yet)

## Performance Characteristics

### Time Complexity

- **add()**: O(n) - sum all numbers
- **subtract()**: O(n) - iterate through numbers
- **multiply()**: O(n) - iterate through numbers
- **divide()**: O(n) - iterate through numbers

Where n = number of arguments

### Space Complexity

- O(1) - All operations use constant space
- argparse creates list of numbers: O(n)

### Benchmarks

For typical usage (2-10 numbers):
- Operation execution: <1ms
- CLI overhead: ~50ms (argparse, Python startup)
- Total time: ~50-100ms per command

## Future Considerations

### Potential Enhancements

**New Operations:**
- Power/exponentiation
- Modulo
- Square root, nth root
- Trigonometric functions
- Logarithms

**New Features:**
- Configuration file support (.mathclirc)
- History/memory features (store last result)
- Expression evaluation ("2 + 3 * 4")
- Interactive REPL mode
- Output formatting (precision, scientific notation)
- Pipe support (read from stdin)

**Architecture Changes for Scaling:**

If adding complex features, consider:
- **Parser module**: For expression evaluation
- **Config module**: For settings management
- **Plugin system**: For extensible operations
- **Formatter module**: For output customization
- **History module**: For result storage

### Scaling Considerations

Current architecture works well for:
- Simple operations on 2-10 numbers
- Command-line one-off calculations
- Scripting and automation

For advanced features, would need:
- Expression parser (infix notation)
- State management (for memory/history)
- More sophisticated error handling
- Configuration system

## Comparison with Alternatives

### vs. bc (Unix calculator)

**mathcli advantages:**
- Simpler syntax for basic operations
- Better error messages
- Cross-platform (Windows included)
- Easier to extend

**bc advantages:**
- More operations built-in
- Expression evaluation
- Programming language features
- Arbitrary precision

### vs. Python -c

**mathcli advantages:**
- Simpler for non-programmers
- Consistent interface
- Better error handling
- Clearer syntax

**Python advantages:**
- Full programming language
- Access to math library
- More flexible
- No installation needed

## Conclusion

mathcli's architecture prioritizes:
- **Simplicity**: Easy to understand and maintain
- **Testability**: High test coverage, clear boundaries
- **Extensibility**: Easy to add new operations
- **Reliability**: Comprehensive error handling
- **Portability**: Works anywhere Python 3.8+ runs

The clean separation between CLI and logic, combined with comprehensive testing, makes mathcli a solid foundation for a calculator CLI tool.
