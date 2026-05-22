try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    int("hello")
except ValueError as err:
    print(f"Error: {err}")

try:
    print([1, 2, 3][10])
except IndexError:
    print("Index out of range!")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("error")
else:
    print(f"Result: {result}")

try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done - always executed")

try:
    x = -1
    if x < 0:
        raise ValueError("Value must be non-negative")
except ValueError as e:
    print(f"Error: {e}")


def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    print(f"Hello, {name}!")


try:
    greet(42)
except TypeError as e:
    print(f"Error: {e}")


class NegativeValueError(ValueError):
    """Zgłaszany gdy wartość jest ujemna."""
    pass


def calculate_discount(price, discount):
    if price < 0:
        raise NegativeValueError(f"Price cannot be negative: {price}")
    if not 0 <= discount <= 100:
        raise ValueError(f"Discount must be 0-100, got: {discount}")
    return price * (1 - discount / 100)


try:
    calculate_discount(-10, 20)
except NegativeValueError as e:
    print(f"NegativeValueError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")

print(calculate_discount(100, 20))
