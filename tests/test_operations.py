"""Unit tests for mathematical operations."""

import pytest
from mathcli.operations import add, subtract, multiply, divide


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


class TestDivide:
    """Test cases for the divide operation."""

    def test_divide_two_numbers(self):
        """Test dividing two integers."""
        assert divide(20, 4) == 5.0

    def test_divide_multiple_numbers(self):
        """Test dividing multiple numbers (left-to-right)."""
        assert divide(100, 2, 5) == 10.0

    def test_divide_floats(self):
        """Test dividing floating-point numbers."""
        assert divide(10.0, 2.5) == 4.0

    def test_divide_with_precision(self):
        """Test division with decimal precision."""
        result = divide(10, 3)
        assert abs(result - 3.333333333333333) < 1e-10

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-20, 4) == -5.0
        assert divide(20, -4) == -5.0
        assert divide(-20, -4) == 5.0

    def test_divide_mixed_types(self):
        """Test dividing mix of integers and floats."""
        assert divide(10, 2.5) == 4.0

    def test_divide_large_numbers(self):
        """Test dividing very large numbers."""
        assert divide(1e20, 1e10) == 1e10

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5.0

    def test_divide_result_less_than_one(self):
        """Test division resulting in number less than 1."""
        assert divide(1, 2) == 0.5

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_by_zero_in_sequence(self):
        """Test that zero in sequence raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(100, 2, 0, 5)

    def test_divide_insufficient_arguments(self):
        """Test that divide requires at least 2 numbers."""
        with pytest.raises(ValueError, match="divide requires at least 2 numbers"):
            divide(5)

    def test_divide_no_arguments(self):
        """Test that divide requires at least 2 numbers."""
        with pytest.raises(ValueError, match="divide requires at least 2 numbers"):
            divide()
