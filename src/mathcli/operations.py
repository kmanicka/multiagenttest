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


def subtract(*numbers: float) -> float:
    """Subtract numbers from left to right.

    Subtracts all subsequent numbers from the first number.
    For example: subtract(10, 3, 2) = 10 - 3 - 2 = 5

    Args:
        *numbers: Variable number of numeric arguments (minimum 2)

    Returns:
        float: The result of the subtraction

    Raises:
        ValueError: If fewer than 2 numbers provided

    Examples:
        >>> subtract(10, 3)
        7.0
        >>> subtract(100, 25, 10, 5)
        60.0
        >>> subtract(5, 10)
        -5.0
    """
    if len(numbers) < 2:
        raise ValueError("subtract requires at least 2 numbers")

    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


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


def divide(*numbers: float) -> float:
    """Divide numbers from left to right.

    Divides the first number by all subsequent numbers.
    For example: divide(100, 2, 5) = 100 / 2 / 5 = 10.0

    Args:
        *numbers: Variable number of numeric arguments (minimum 2)

    Returns:
        float: The result of the division

    Raises:
        ValueError: If fewer than 2 numbers provided
        ZeroDivisionError: If attempting to divide by zero

    Examples:
        >>> divide(20, 4)
        5.0
        >>> divide(100, 2, 5)
        10.0
        >>> divide(-20, 4)
        -5.0
    """
    if len(numbers) < 2:
        raise ValueError("divide requires at least 2 numbers")

    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= num
    return result


def absolute_value(number: float) -> float:
    """Return the absolute value of a number.

    The absolute value is the non-negative value of a number,
    representing its distance from zero.

    Args:
        number: The number to get absolute value of

    Returns:
        float: The absolute value (non-negative)

    Examples:
        >>> absolute_value(-10.5)
        10.5
        >>> absolute_value(5)
        5.0
        >>> absolute_value(0)
        0.0
    """
    return abs(number)


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b.

    Uses Python's modulo operator which follows the sign of the divisor.
    For example: -10 % 3 = 2 (not -1)

    Args:
        a: The dividend
        b: The divisor

    Returns:
        float: The remainder

    Raises:
        ValueError: If divisor is zero

    Examples:
        >>> modulo(10, 3)
        1.0
        >>> modulo(10, 5)
        0.0
        >>> modulo(10.5, 3)
        1.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
