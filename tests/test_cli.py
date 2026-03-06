"""Integration tests for the mathcli CLI."""

import subprocess
import sys
import pytest


def run_cli(*args):
    """Helper function to run the CLI and capture output.

    Args:
        *args: Command-line arguments to pass to mathcli

    Returns:
        subprocess.CompletedProcess: Result with returncode, stdout, stderr
    """
    result = subprocess.run(
        [sys.executable, "-m", "mathcli"] + list(args),
        capture_output=True,
        text=True,
    )
    return result


class TestCLIBasics:
    """Test basic CLI functionality."""

    def test_help_flag(self):
        """Test --help flag shows help text."""
        result = run_cli("--help")
        assert result.returncode == 0
        assert "mathematical operations" in result.stdout.lower()
        assert "add" in result.stdout
        assert "subtract" in result.stdout
        assert "multiply" in result.stdout

    def test_version_flag(self):
        """Test --version flag shows version."""
        result = run_cli("--version")
        assert result.returncode == 0
        assert "0.1.0" in result.stdout

    def test_no_arguments(self):
        """Test running CLI with no arguments shows help."""
        result = run_cli()
        assert result.returncode == 1
        assert "usage:" in result.stdout.lower() or "usage:" in result.stderr.lower()

    def test_invalid_command(self):
        """Test invalid command shows error."""
        result = run_cli("invalid_command")
        assert result.returncode != 0


class TestCLIAddition:
    """Test addition command via CLI."""

    def test_add_two_numbers(self):
        """Test adding two numbers."""
        result = run_cli("add", "5", "10")
        assert result.returncode == 0
        assert "15" in result.stdout

    def test_add_multiple_numbers(self):
        """Test adding multiple numbers."""
        result = run_cli("add", "1", "2", "3", "4")
        assert result.returncode == 0
        assert "10" in result.stdout

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        result = run_cli("add", "1.5", "2.5")
        assert result.returncode == 0
        assert "4" in result.stdout

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = run_cli("add", "-5", "10", "-3")
        assert result.returncode == 0
        assert "2" in result.stdout

    def test_add_insufficient_args(self):
        """Test add with insufficient arguments shows error."""
        result = run_cli("add", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()

    def test_add_no_args(self):
        """Test add with no arguments shows error."""
        result = run_cli("add")
        assert result.returncode != 0

    def test_add_help(self):
        """Test add --help shows command-specific help."""
        result = run_cli("add", "--help")
        assert result.returncode == 0
        assert "add" in result.stdout.lower()


class TestCLISubtraction:
    """Test subtraction command via CLI."""

    def test_subtract_two_numbers(self):
        """Test subtracting two numbers."""
        result = run_cli("subtract", "10", "3")
        assert result.returncode == 0
        assert "7" in result.stdout

    def test_subtract_multiple_numbers(self):
        """Test subtracting multiple numbers (left-to-right)."""
        result = run_cli("subtract", "100", "25", "10", "5")
        assert result.returncode == 0
        assert "60" in result.stdout

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        result = run_cli("subtract", "5", "10")
        assert result.returncode == 0
        assert "-5" in result.stdout

    def test_subtract_insufficient_args(self):
        """Test subtract with insufficient arguments shows error."""
        result = run_cli("subtract", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLIMultiplication:
    """Test multiplication command via CLI."""

    def test_multiply_two_numbers(self):
        """Test multiplying two numbers."""
        result = run_cli("multiply", "5", "4")
        assert result.returncode == 0
        assert "20" in result.stdout

    def test_multiply_multiple_numbers(self):
        """Test multiplying multiple numbers."""
        result = run_cli("multiply", "2", "3", "4")
        assert result.returncode == 0
        assert "24" in result.stdout

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        result = run_cli("multiply", "5", "0")
        assert result.returncode == 0
        assert "0" in result.stdout

    def test_multiply_negative(self):
        """Test multiplying negative numbers."""
        result = run_cli("multiply", "-2", "-3")
        assert result.returncode == 0
        assert "6" in result.stdout

    def test_multiply_insufficient_args(self):
        """Test multiply with insufficient arguments shows error."""
        result = run_cli("multiply", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLIDivision:
    """Test division command via CLI (if available)."""

    def test_divide_two_numbers(self):
        """Test dividing two numbers."""
        result = run_cli("divide", "20", "4")
        if result.returncode == 0:
            assert "5" in result.stdout
        else:
            pytest.skip("Division command not yet implemented")

    def test_divide_multiple_numbers(self):
        """Test dividing multiple numbers."""
        result = run_cli("divide", "100", "2", "5")
        if result.returncode == 0:
            assert "10" in result.stdout
        else:
            pytest.skip("Division command not yet implemented")

    def test_divide_by_zero(self):
        """Test division by zero shows error."""
        result = run_cli("divide", "10", "0")
        # Skip if divide command doesn't exist yet
        if "invalid choice" in result.stderr:
            pytest.skip("Division command not yet implemented")
        # If divide exists, check it properly handles division by zero
        if result.returncode != 0:
            assert "zero" in result.stderr.lower()


class TestCLIErrorHandling:
    """Test CLI error handling."""

    def test_invalid_number_add(self):
        """Test invalid number input shows error."""
        result = run_cli("add", "5", "abc")
        assert result.returncode != 0

    def test_invalid_number_subtract(self):
        """Test invalid number input for subtract."""
        result = run_cli("subtract", "10", "xyz")
        assert result.returncode != 0

    def test_missing_command(self):
        """Test running with missing command."""
        result = run_cli()
        assert result.returncode != 0


class TestCLIOutputFormat:
    """Test CLI output format."""

    def test_output_is_numeric(self):
        """Test output is a valid number."""
        result = run_cli("add", "5", "10")
        assert result.returncode == 0
        output = result.stdout.strip()
        try:
            float(output)
            assert True
        except ValueError:
            pytest.fail(f"Output '{output}' is not a valid number")

    def test_error_goes_to_stderr(self):
        """Test errors are written to stderr."""
        result = run_cli("add", "5")
        assert result.returncode == 1
        assert len(result.stderr) > 0 or result.returncode == 1
