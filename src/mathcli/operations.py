"""Mathematical operations for the mathcli tool.

This module contains implementations of basic mathematical operations.
"""


def add(*numbers: float) -> float:
    """Add two or more numbers together.

    Args:
        *numbers: Variable number of numeric arguments to add

    Returns:
        float: The sum of all numbers

    Raises:
        ValueError: If fewer than 2 numbers provided

    Examples:
        >>> add(5, 10)
        15.0
        >>> add(1.5, 2.5, 3.0)
        7.0
        >>> add(-5, 10, -3)
        2.0
    """
    if len(numbers) < 2:
        raise ValueError("add requires at least 2 numbers")
    return sum(numbers)


def multiply(*numbers: float) -> float:
    """Multiply two or more numbers together.

    Args:
        *numbers: Variable number of numeric arguments to multiply

    Returns:
        float: The product of all numbers

    Raises:
        ValueError: If fewer than 2 numbers provided

    Examples:
        >>> multiply(5, 4)
        20.0
        >>> multiply(2, 3, 4)
        24.0
        >>> multiply(-2, -3)
        6.0
    """
    if len(numbers) < 2:
        raise ValueError("multiply requires at least 2 numbers")

    result = 1
    for num in numbers:
        result *= num
    return result
