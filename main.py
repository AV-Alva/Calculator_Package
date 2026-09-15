"""Demonstration program for calculator_tools."""

"""Reusable calculator tools package."""

from calculator_tools import (
    add,
    subtract,
    multiply,
    divide,
    percentage,
    average,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_length,
    InvalidOperationError,
)


def main():
    """Demonstrate calculator_tools functionality."""

    print("----- ARITHMETIC -----")

    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))

    print("\n----- PERCENTAGE -----")

    print("Percentage:", percentage(450, 500), "%")

    print("\n----- STATISTICS -----")

    marks = [80, 90, 75, 85, 95]
    print("Average:", average(marks))

    print("\n----- TEMPERATURE -----")

    print("30°C =", celsius_to_fahrenheit(30), "°F")
    print("86°F =", fahrenheit_to_celsius(86), "°C")

    print("\n----- UNIT CONVERSION -----")

    print("5 km =", convert_length(5, "km_to_m"), "metres")
    print("2500 m =", convert_length(2500, "m_to_km"), "km")

    print("\n----- ERROR HANDLING -----")

    try:
        print(divide(10, 0))

    except ZeroDivisionError as error:
        print("Error:", error)

    try:
        print(average([10, "twenty", 30]))

    except TypeError as error:
        print("Error:", error)

    try:
        print(convert_length(10, "invalid_conversion"))

    except InvalidOperationError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()