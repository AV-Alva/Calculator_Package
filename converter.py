"""Temperature and unit conversion functions."""

from exceptions import InvalidOperationError


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""

    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be numeric.")

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""

    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temperature must be numeric.")

    return (fahrenheit - 32) * 5 / 9


def convert_length(value, operation):
    """Perform basic length conversions."""

    if not isinstance(value, (int, float)):
        raise TypeError("Value must be numeric.")

    if operation == "km_to_m":
        return value * 1000

    elif operation == "m_to_km":
        return value / 1000

    elif operation == "cm_to_m":
        return value / 100

    elif operation == "m_to_cm":
        return value * 100

    else:
        raise InvalidOperationError(
            f"Unsupported conversion: {operation}"
        )