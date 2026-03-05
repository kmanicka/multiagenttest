"""Unit tests for mathematical operations."""

import pytest
from mathcli.operations import add, subtract, multiply


class TestAdd:
    """Test cases for the add operation."""

    def test_add_two_numbers(self):
        """Test adding two integers."""
        assert add(5, 10) == 15

    def test_add_multiple_numbers(self):
        """Test adding multiple integers."""
        assert add(1, 2, 3, 4, 5) == 15

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        assert add(1.5, 2.5, 3.0) == 7.0

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-5, 10, -3) == 2

    def test_add_mixed_types(self):
        """Test adding mix of integers and floats."""
        assert add(5, 2.5) == 7.5

    def test_add_large_numbers(self):
        """Test adding very large numbers."""
        assert add(1e10, 2e10) == 3e10

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_add_insufficient_arguments(self):
        """Test that add requires at least 2 numbers."""
        with pytest.raises(ValueError, match="add requires at least 2 numbers"):
            add(5)

    def test_add_no_arguments(self):
        """Test that add requires at least 2 numbers."""
        with pytest.raises(ValueError, match="add requires at least 2 numbers"):
            add()


class TestSubtract:
    """Test cases for the subtract operation."""

    def test_subtract_two_numbers(self):
        """Test subtracting two integers."""
        assert subtract(10, 3) == 7

    def test_subtract_multiple_numbers(self):
        """Test subtracting multiple numbers (left-to-right)."""
        assert subtract(100, 25, 10, 5) == 60

    def test_subtract_floats(self):
        """Test subtracting floating-point numbers."""
        assert subtract(10.5, 2.5, 1.0) == 7.0

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        assert subtract(5, 10) == -5

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -10) == 5
        assert subtract(-5, 10) == -15
        assert subtract(10, -5) == 15

    def test_subtract_mixed_types(self):
        """Test subtracting mix of integers and floats."""
        assert subtract(10, 2.5) == 7.5

    def test_subtract_large_numbers(self):
        """Test subtracting very large numbers."""
        assert subtract(1e10, 2e9) == 8e9

    def test_subtract_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_same_number(self):
        """Test subtracting same number results in zero."""
        assert subtract(5, 5) == 0

    def test_subtract_insufficient_arguments(self):
        """Test that subtract requires at least 2 numbers."""
        with pytest.raises(ValueError, match="subtract requires at least 2 numbers"):
            subtract(5)

    def test_subtract_no_arguments(self):
        """Test that subtract requires at least 2 numbers."""
        with pytest.raises(ValueError, match="subtract requires at least 2 numbers"):
            subtract()


class TestMultiply:
    """Test cases for the multiply operation."""

    def test_multiply_two_numbers(self):
        """Test multiplying two integers."""
        assert multiply(5, 4) == 20

    def test_multiply_multiple_numbers(self):
        """Test multiplying multiple numbers."""
        assert multiply(2, 3, 4) == 24

    def test_multiply_floats(self):
        """Test multiplying floating-point numbers."""
        assert multiply(2.5, 4.0) == 10.0
        assert multiply(1.5, 2.0, 3.0) == 9.0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-5, 4) == -20
        assert multiply(-2, -3) == 6
        assert multiply(-1, -1, -1) == -1

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(5, 0, 3) == 0

    def test_multiply_mixed_types(self):
        """Test multiplying mix of integers and floats."""
        assert multiply(5, 2.5) == 12.5

    def test_multiply_large_numbers(self):
        """Test multiplying very large numbers."""
        assert multiply(1e10, 1e10) == 1e20

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5

    def test_multiply_insufficient_arguments(self):
        """Test that multiply requires at least 2 numbers."""
        with pytest.raises(ValueError, match="multiply requires at least 2 numbers"):
            multiply(5)

    def test_multiply_no_arguments(self):
        """Test that multiply requires at least 2 numbers."""
        with pytest.raises(ValueError, match="multiply requires at least 2 numbers"):
            multiply()
