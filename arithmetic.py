"""Basic arithmetic operations."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def percentage(value, total):
    """Calculate percentage."""

    if total == 0:
        raise ValueError("Total cannot be zero.")

    return (value / total) * 100