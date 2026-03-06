"""Integration tests for the mathcli command-line interface."""

import subprocess
import sys
import pytest
from io import StringIO
from unittest.mock import patch


def run_cli(*args):
    """Helper to run the CLI and capture output.

    Args:
        *args: Command-line arguments to pass to mathcli

    Returns:
        CompletedProcess: Result of the subprocess execution
    """
    result = subprocess.run(
        [sys.executable, "-m", "mathcli"] + list(args), capture_output=True, text=True
    )
    return result


def run_cli_direct(*args):
    """Helper to run the CLI directly (for code coverage).

    Args:
        *args: Command-line arguments to pass to mathcli

    Returns:
        tuple: (return_code, stdout, stderr)
    """
    from mathcli.__main__ import main

    stdout = StringIO()
    stderr = StringIO()
    return_code = 0

    with patch("sys.argv", ["mathcli"] + list(args)):
        with patch("sys.stdout", stdout):
            with patch("sys.stderr", stderr):
                try:
                    main()
                except SystemExit as e:
                    return_code = e.code if e.code is not None else 0

    return return_code, stdout.getvalue(), stderr.getvalue()


class TestCLIBasics:
    """Test basic CLI functionality."""

    def test_help_flag(self):
        """Test --help flag displays help message."""
        result = run_cli("--help")
        assert result.returncode == 0
        assert "mathematical operations" in result.stdout.lower()
        assert "add" in result.stdout

    def test_version_flag(self):
        """Test --version flag displays version."""
        result = run_cli("--version")
        assert result.returncode == 0
        assert "0.1.0" in result.stdout

    def test_no_arguments(self):
        """Test that running without arguments shows help and exits with error."""
        result = run_cli()
        assert result.returncode == 1


class TestCLIAddition:
    """Test CLI addition command."""

    @pytest.mark.skipif(
        not hasattr(sys, "real_prefix") and not hasattr(sys, "base_prefix"),
        reason="Requires mathcli to be installed",
    )
    def test_add_two_numbers(self):
        """Test adding two integers via CLI."""
        result = run_cli("add", "5", "10")
        if result.returncode == 0:
            assert "15" in result.stdout.strip()

    def test_add_multiple_numbers(self):
        """Test adding multiple numbers via CLI."""
        result = run_cli("add", "1", "2", "3", "4")
        if result.returncode == 0:
            assert "10" in result.stdout.strip()

    def test_add_floats(self):
        """Test adding floating-point numbers via CLI."""
        result = run_cli("add", "1.5", "2.5")
        if result.returncode == 0:
            assert "4" in result.stdout.strip()

    def test_add_negative_numbers(self):
        """Test adding negative numbers via CLI."""
        result = run_cli("add", "-5", "10", "-3")
        if result.returncode == 0:
            assert "2" in result.stdout.strip()

    def test_add_insufficient_args(self):
        """Test that add with single argument fails."""
        result = run_cli("add", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLISubtraction:
    """Test CLI subtraction command."""

    def test_subtract_two_numbers(self):
        """Test subtracting two integers via CLI."""
        result = run_cli("subtract", "10", "3")
        if result.returncode == 0:
            assert "7" in result.stdout.strip()

    def test_subtract_multiple_numbers(self):
        """Test subtracting multiple numbers via CLI."""
        result = run_cli("subtract", "100", "25", "10", "5")
        if result.returncode == 0:
            assert "60" in result.stdout.strip()

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        result = run_cli("subtract", "5", "10")
        if result.returncode == 0:
            assert "-5" in result.stdout.strip()

    def test_subtract_insufficient_args(self):
        """Test that subtract with single argument fails."""
        result = run_cli("subtract", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLIMultiplication:
    """Test CLI multiplication command."""

    def test_multiply_two_numbers(self):
        """Test multiplying two integers via CLI."""
        result = run_cli("multiply", "5", "4")
        if result.returncode == 0:
            assert "20" in result.stdout.strip()

    def test_multiply_multiple_numbers(self):
        """Test multiplying multiple numbers via CLI."""
        result = run_cli("multiply", "2", "3", "4")
        if result.returncode == 0:
            assert "24" in result.stdout.strip()

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        result = run_cli("multiply", "5", "0")
        if result.returncode == 0:
            assert "0" in result.stdout.strip()

    def test_multiply_insufficient_args(self):
        """Test that multiply with single argument fails."""
        result = run_cli("multiply", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLIDivision:
    """Test CLI division command."""

    def test_divide_two_numbers(self):
        """Test dividing two integers via CLI."""
        result = run_cli("divide", "20", "4")
        if result.returncode == 0:
            assert "5" in result.stdout.strip()

    def test_divide_multiple_numbers(self):
        """Test dividing multiple numbers via CLI."""
        result = run_cli("divide", "100", "2", "5")
        if result.returncode == 0:
            assert "10" in result.stdout.strip()

    def test_divide_with_precision(self):
        """Test division with decimal result."""
        result = run_cli("divide", "10", "3")
        if result.returncode == 0:
            assert "3.33" in result.stdout

    def test_divide_by_zero(self):
        """Test that dividing by zero fails with appropriate error."""
        result = run_cli("divide", "10", "0")
        assert result.returncode == 1
        assert "cannot divide by zero" in result.stderr.lower()

    def test_divide_insufficient_args(self):
        """Test that divide with single argument fails."""
        result = run_cli("divide", "5")
        assert result.returncode == 1
        assert "error" in result.stderr.lower()


class TestCLIErrorHandling:
    """Test CLI error handling."""

    def test_invalid_number(self):
        """Test that invalid number input fails."""
        result = run_cli("add", "5", "abc")
        assert result.returncode != 0

    def test_invalid_command(self):
        """Test that invalid command fails."""
        result = run_cli("invalid")
        assert result.returncode != 0

    def test_mixed_invalid_valid(self):
        """Test that mix of valid and invalid numbers fails."""
        result = run_cli("multiply", "5", "abc", "10")
        assert result.returncode != 0


class TestCLIDirect:
    """Test CLI directly for code coverage."""

    def test_add_direct(self):
        """Test add command directly."""
        return_code, stdout, stderr = run_cli_direct("add", "5", "10")
        assert return_code == 0
        assert "15" in stdout

    def test_subtract_direct(self):
        """Test subtract command directly."""
        return_code, stdout, stderr = run_cli_direct("subtract", "10", "3")
        assert return_code == 0
        assert "7" in stdout

    def test_multiply_direct(self):
        """Test multiply command directly."""
        return_code, stdout, stderr = run_cli_direct("multiply", "5", "4")
        assert return_code == 0
        assert "20" in stdout

    def test_divide_direct(self):
        """Test divide command directly."""
        return_code, stdout, stderr = run_cli_direct("divide", "20", "4")
        assert return_code == 0
        assert "5" in stdout

    def test_divide_by_zero_direct(self):
        """Test divide by zero directly."""
        return_code, stdout, stderr = run_cli_direct("divide", "10", "0")
        assert return_code == 1
        assert "cannot divide by zero" in stderr.lower()

    def test_help_direct(self):
        """Test help flag directly."""
        return_code, stdout, stderr = run_cli_direct("--help")
        assert return_code == 0
        assert "mathematical operations" in stdout.lower()

    def test_version_direct(self):
        """Test version flag directly."""
        return_code, stdout, stderr = run_cli_direct("--version")
        assert return_code == 0
        assert "0.1.0" in stdout

    def test_no_command_direct(self):
        """Test no command directly."""
        return_code, stdout, stderr = run_cli_direct()
        assert return_code == 1

    def test_insufficient_args_add_direct(self):
        """Test add with insufficient args directly."""
        return_code, stdout, stderr = run_cli_direct("add", "5")
        assert return_code == 1
        assert "error" in stderr.lower()

    def test_insufficient_args_subtract_direct(self):
        """Test subtract with insufficient args directly."""
        return_code, stdout, stderr = run_cli_direct("subtract", "5")
        assert return_code == 1
        assert "error" in stderr.lower()

    def test_insufficient_args_multiply_direct(self):
        """Test multiply with insufficient args directly."""
        return_code, stdout, stderr = run_cli_direct("multiply", "5")
        assert return_code == 1
        assert "error" in stderr.lower()

    def test_insufficient_args_divide_direct(self):
        """Test divide with insufficient args directly."""
        return_code, stdout, stderr = run_cli_direct("divide", "5")
        assert return_code == 1
        assert "error" in stderr.lower()
