"""Unit tests for mathematical operations."""

import pytest
from mathcli.operations import add


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
