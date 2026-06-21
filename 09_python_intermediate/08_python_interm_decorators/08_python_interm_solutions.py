# Solutions: 08_python_interm_decorators.ipynb
from functools import wraps
from dataclasses import dataclass, field
from datetime import date
import math

##############################################################################
# 1. shout
##############################################################################

def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"!!! {result} !!!"
    return wrapper


@shout
def greet(name):
    return f"hello {name}"


print(greet("Alice"))   # !!! hello Alice !!!

##############################################################################
# 2. print_args
##############################################################################

def print_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"arg type: {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper


@print_args
def echo(value):
    return value


echo("hello")   # arg type: str
echo(42)        # arg type: int

##############################################################################
# 3. count_calls
##############################################################################

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls
def say_hi():
    print("hi")


say_hi()
say_hi()
say_hi()
print(say_hi.calls)   # 3

##############################################################################
# 4. repeat(n)
##############################################################################

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def ping():
    print("ping")
    return "ok"


result = ping()   # ping  ping  ping
print(result)     # ok

##############################################################################
# 5. validate_type
##############################################################################

def validate_type(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and not isinstance(args[0], expected_type):
                raise TypeError(
                    f"Expected {expected_type.__name__}, "
                    f"got {type(args[0]).__name__}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_type(str)
def shout_text(text):
    return text.upper()


print(shout_text("hello"))   # HELLO
try:
    shout_text(123)
except TypeError as e:
    print(e)                 # Expected str, got int

##############################################################################
# 6. retry(times)
##############################################################################

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {i + 1} failed: {e}")
            raise last_error
        return wrapper
    return decorator


attempt = 0


@retry(3)
def flaky():
    global attempt
    attempt += 1
    if attempt < 3:
        raise RuntimeError(f"Fail #{attempt}")
    return "success"


print(flaky())   # success (after 2 failures)

##############################################################################
# 7. debug with @wraps
##############################################################################

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@debug
def greet(name):
    """Return a greeting."""
    return f"hello {name}"


print(greet("Alice"))     # Calling: greet \n hello Alice
print(greet.__name__)     # greet
print(greet.__doc__)      # Return a greeting.

##############################################################################
# 8. Converter - @staticmethod
##############################################################################

class Converter:
    @staticmethod
    def km_to_miles(km):
        return round(km * 0.621371, 4)

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32


print(Converter.km_to_miles(100))          # 62.1371
print(Converter.celsius_to_fahrenheit(0))   # 32.0

##############################################################################
# 9. Date - @classmethod
##############################################################################

class Date:
    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day

    @classmethod
    def from_string(cls, s):
        year, month, day = (int(p) for p in s.split('-'))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        d = date.today()
        return cls(d.year, d.month, d.day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


d = Date.from_string("2026-03-24")
print(d)            # 2026-03-24
print(Date.today()) # current date

##############################################################################
# 10. Rectangle with @property
##############################################################################

class Rectangle:
    def __init__(self, width, height):
        self._width  = None
        self._height = None
        self.width   = width
        self.height  = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20
try:
    r.width = -1
except ValueError as e:
    print(e)        # Width must be positive

##############################################################################
# 11. Book - @dataclass
##############################################################################

@dataclass
class Book:
    title:  str
    author: str
    year:   int

    def age(self):
        return 2026 - self.year


b = Book("1984", "Orwell", 1949)
print(b)          # Book(title='1984', author='Orwell', year=1949)
print(b.age())    # 77

##############################################################################
# 12. Coordinate - @dataclass(frozen=True)
##############################################################################

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


warsaw  = Coordinate(52.2297, 21.0122)
warsaw2 = Coordinate(52.2297, 21.0122)
print(warsaw == warsaw2)   # True

locations = {warsaw: "Warsaw"}
print(locations[warsaw2])  # Warsaw

##############################################################################
# 13. Student with grades list
##############################################################################

@dataclass
class Student:
    name:   str
    grades: list = field(default_factory=list)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


s = Student("Alice")
s.grades = [90, 85, 92]
print(s.average())               # 89.0
print(Student("Bob").average())  # 0.0
