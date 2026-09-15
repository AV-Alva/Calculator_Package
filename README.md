# Calculator Tools — Reusable Python Package

## Project Overview

This project demonstrates how to create and use a **reusable Python package** instead of writing all functionality inside a single Python file.

The project is organized into separate Python modules based on their responsibilities.

The `calculator_tools` package provides functionality for:

* Basic arithmetic operations
* Percentage calculation
* Average calculation
* Temperature conversion
* Length/unit conversion
* Input validation
* Exception handling
* Custom exceptions

The main objective of this project is to understand the difference between a **function, module, package, and import**, and to learn how multiple Python files can work together as one application.

---

## Project Structure

```text
calculator_tools_project/
│
├── calculator_tools/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── statistics.py
│   ├── converter.py
│   ├── exceptions.py
│   └── main.py
│
├── README.md
└── .gitignore
```

`calculator_tools` is the Python **package**, while the `.py` files inside it are individual **modules**.

---

# Package Modules

## 1. `__init__.py`

The `__init__.py` file is the initialization file for the `calculator_tools` package.

It can be used to expose selected functions and classes from different modules at the package level.

Example:

```python
from .arithmetic import add, subtract, multiply, divide, percentage
from .statistics import average
from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_length,
)
from .exceptions import InvalidOperationError
```

The `.` represents the **current package**.

For example:

```python
from .arithmetic import add
```

means:

```text
Current package
      ↓
calculator_tools
      ↓
arithmetic.py
      ↓
add()
```

---

## 2. `arithmetic.py`

The `arithmetic.py` module contains functions related to basic mathematical operations.

It provides:

* `add()` — adds two numbers
* `subtract()` — subtracts two numbers
* `multiply()` — multiplies two numbers
* `divide()` — divides two numbers
* `percentage()` — calculates a percentage

Example:

```python
add(10, 5)
```

returns:

```text
15
```

The division function also checks for division by zero.

Example:

```python
divide(10, 0)
```

raises:

```text
ZeroDivisionError
```

This prevents the application from performing an invalid mathematical operation.

---

## 3. `statistics.py`

The `statistics.py` module contains functions used for statistical calculations.

Currently, it provides:

```python
average()
```

Example:

```python
average([80, 90, 70])
```

Calculation:

```text
80 + 90 + 70 = 240

240 / 3 = 80
```

Therefore, the function returns:

```text
80
```

The function also validates the input.

It handles:

* Input that is not a list
* Empty lists
* Non-numeric values inside the list

Examples of invalid input include:

```python
average([])
```

and:

```python
average([10, "twenty", 30])
```

These conditions are handled using appropriate exceptions such as `ValueError` and `TypeError`.

---

## 4. `converter.py`

The `converter.py` module contains functions for temperature and length conversions.

### Temperature Conversions

The module supports:

* Celsius to Fahrenheit
* Fahrenheit to Celsius

Example:

```python
celsius_to_fahrenheit(30)
```

returns approximately:

```text
86°F
```

### Length Conversions

The module supports:

* Kilometres to metres
* Metres to kilometres
* Centimetres to metres
* Metres to centimetres

Example:

```python
convert_length(5, "km_to_m")
```

returns:

```text
5000
```

The converter module also validates the input type and checks whether the requested conversion operation is supported.

---

## 5. `exceptions.py`

The `exceptions.py` module contains the custom exception created for this project.

The custom exception is:

```python
class InvalidOperationError(Exception):
    """Raised when an unsupported operation is requested."""
    pass
```

`InvalidOperationError` inherits from Python's built-in `Exception` class.

It is used when a user requests an operation that the package does not support.

Example:

```python
convert_length(10, "invalid_conversion")
```

raises:

```text
InvalidOperationError
```

This provides a clearer and more meaningful error than using a generic exception.

---

## 6. `main.py`

The `main.py` module demonstrates how the different modules inside the package can work together.

Because `main.py` is located inside the `calculator_tools` package, it uses **relative imports**.

Example:

```python
from .arithmetic import add, subtract, multiply, divide, percentage

from .statistics import average

from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_length,
)

from .exceptions import InvalidOperationError
```

The `.` means:

> Import from the current package.

For example:

```python
from .statistics import average
```

means:

```text
calculator_tools
      ↓
statistics.py
      ↓
average()
```

The `main.py` module demonstrates:

* Arithmetic calculations
* Percentage calculation
* Average calculation
* Temperature conversion
* Unit conversion
* Division-by-zero handling
* Incorrect data-type handling
* Unsupported-operation handling
* Use of the custom `InvalidOperationError`

---

# Function vs Module vs Package vs Import

## Function

A **function** is a reusable block of code designed to perform a particular task.

Example:

```python
def add(a, b):
    return a + b
```

Here:

```text
add()
```

is a function.

---

## Module

A **module** is a Python file containing related Python code.

For example:

```text
arithmetic.py
```

is a module containing related mathematical functions:

```text
add()
subtract()
multiply()
divide()
percentage()
```

Another example is:

```text
converter.py
```

which contains conversion-related functions.

---

## Package

A **package** is a directory used to organize related Python modules.

In this project:

```text
calculator_tools/
```

is the package.

It contains:

```text
arithmetic.py
statistics.py
converter.py
exceptions.py
main.py
```

This allows the application to be divided into smaller, logically organized components.

---

## Import

An **import** allows one Python module to use functionality defined in another module.

For example, inside `main.py`:

```python
from .arithmetic import add
```

imports the `add()` function from the `arithmetic.py` module in the current package.

The relationship can be visualized as:

```text
FUNCTION
   ↓
add()

lives inside

MODULE
   ↓
arithmetic.py

lives inside

PACKAGE
   ↓
calculator_tools/

used by another module through

IMPORT
   ↓
from .arithmetic import add
```

---

# Relative Imports

This project uses **relative imports** because the modules belong to the same package.

For example:

```python
from .arithmetic import add
```

The dot:

```text
.
```

means:

```text
current package
```

Therefore:

```python
from .arithmetic import add
```

can be understood as:

```text
From the arithmetic module
inside my current calculator_tools package,
import the add function.
```

Similarly:

```python
from .exceptions import InvalidOperationError
```

imports the custom exception from the `exceptions.py` module inside the same package.

---

# Exception Handling

The project demonstrates different types of errors and exceptions.

| Error Situation       | Exception               |
| --------------------- | ----------------------- |
| Division by zero      | `ZeroDivisionError`     |
| Invalid value         | `ValueError`            |
| Incorrect data type   | `TypeError`             |
| Unsupported operation | `InvalidOperationError` |

---

## Division by Zero

Example:

```python
divide(10, 0)
```

The function raises:

```text
ZeroDivisionError
```

The exception can be handled using:

```python
try:
    print(divide(10, 0))

except ZeroDivisionError as error:
    print("Error:", error)
```

---

## Incorrect Data Type

Example:

```python
average([10, "twenty", 30])
```

The value `"twenty"` is a string instead of a number.

The program raises:

```text
TypeError
```

---

## Invalid Value

Example:

```python
average([])
```

An average cannot be calculated from an empty list.

The program raises:

```text
ValueError
```

---

## Unsupported Operation

Example:

```python
convert_length(10, "invalid_conversion")
```

The requested conversion does not exist.

The program raises the custom exception:

```text
InvalidOperationError
```

---

# How Exception Handling Works

The reusable module is responsible for **detecting and raising** an error.

For example:

```text
converter.py
      ↓
Detect invalid operation
      ↓
raise InvalidOperationError
```

The `main.py` module is responsible for **handling** the error.

```text
main.py
      ↓
try
      ↓
Call function
      ↓
Exception occurs
      ↓
except
      ↓
Display meaningful error
```

This separation keeps the reusable functions clean while allowing the application to decide how errors should be presented.

---

# How to Run the Project

Because `main.py` is located **inside the `calculator_tools` package** and uses relative imports, the program should be executed as a Python module.

Open the terminal in the root project directory:

```text
calculator_tools_project/
```

For example:

```text
PS D:\Projects\calculator_tools_project>
```

Run:

```bash
python -m calculator_tools.main
```

### Important

Do **not** run:

```bash
python calculator_tools/main.py
```

when using relative imports such as:

```python
from .arithmetic import add
```

Running the program using:

```bash
python -m calculator_tools.main
```

tells Python:

> Run `main` as a module belonging to the `calculator_tools` package.

This allows Python to correctly understand what the `.` in the relative imports refers to.

---

# Program Execution Flow

When the following command is executed:

```bash
python -m calculator_tools.main
```

the flow is approximately:

```text
calculator_tools package
          │
          ↓
       main.py
          │
          ├──── imports arithmetic.py
          │
          ├──── imports statistics.py
          │
          ├──── imports converter.py
          │
          └──── imports exceptions.py
          │
          ↓
        main()
          │
          ├──── Arithmetic calculations
          ├──── Percentage calculation
          ├──── Average calculation
          ├──── Temperature conversion
          ├──── Unit conversion
          └──── Exception handling
          │
          ↓
        Output
```

---

# `if __name__ == "__main__"`

The bottom of `main.py` contains:

```python
if __name__ == "__main__":
    main()
```

When the module is executed, this condition ensures that the `main()` function starts the application.

It also prevents `main()` from automatically executing if the module is imported somewhere else.

---

# Example Output

A sample execution may produce:

```text
----- ARITHMETIC -----
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0

----- PERCENTAGE -----
Percentage: 90.0 %

----- STATISTICS -----
Average: 85.0

----- TEMPERATURE -----
30°C = 86.0 °F
86°F = 30.0 °C

----- UNIT CONVERSION -----
5 km = 5000 metres
2500 m = 2.5 km

----- ERROR HANDLING -----
Error: Cannot divide by zero.
Error: All values must be numbers.
Error: Unsupported conversion: invalid_conversion
```

---

# Key Concepts Learned

Through this project, I learned how to:

* Create reusable Python functions
* Organize related functions into modules
* Organize multiple modules into a Python package
* Understand the purpose of `__init__.py`
* Import functions between modules
* Use relative imports
* Run a Python package module using `python -m`
* Separate different responsibilities into different files
* Validate input values and data types
* Use `try` and `except`
* Raise exceptions using `raise`
* Handle built-in Python exceptions
* Create a custom exception
* Reuse functionality instead of rewriting code

---

# Why Use Packages?

A small Python application can be written inside one file.

However, as an application grows, putting everything inside one file makes the code difficult to understand, maintain, test, and reuse.

Instead of:

```text
one_large_program.py
│
├── arithmetic logic
├── statistics logic
├── conversion logic
├── exception definitions
└── main application
```

this project separates responsibilities:

```text
calculator_tools/
│
├── arithmetic.py
├── statistics.py
├── converter.py
├── exceptions.py
└── main.py
```

This provides better:

* Organization
* Readability
* Maintainability
* Reusability
* Separation of responsibilities

---

# Final Learning Summary

The main learning from this project can be summarized as:

```text
FUNCTION
    ↓
Reusable logic

MODULE
    ↓
Python file containing related logic

PACKAGE
    ↓
Collection of related Python modules

IMPORT
    ↓
Use functionality from another module

EXCEPTION HANDLING
    ↓
Handle errors safely

CUSTOM EXCEPTION
    ↓
Represent application-specific errors
```

The project demonstrates how Python code can move from a simple single-file program toward a more structured and reusable application.
