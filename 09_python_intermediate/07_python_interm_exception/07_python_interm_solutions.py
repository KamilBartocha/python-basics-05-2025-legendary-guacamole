# Solutions: 07_python_interm_exception.ipynb
import math

##############################################################################
# 1. safe_open
##############################################################################

def safe_open(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    finally:
        print("--- done ---")


result = safe_open("missing.txt")
print(result)   # None

##############################################################################
# 2. try/except/else - conversion
##############################################################################

value = "42"

try:
    number = int(value)
except ValueError:
    print("Not a number")
else:
    print(number ** 2)   # 1764

##############################################################################
# 3. safe_divide
##############################################################################

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None


print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None
print(safe_divide(10, 'x'))  # None

##############################################################################
# 4. compute - all 4 blocks
##############################################################################

def compute(text, divisor):
    try:
        number = int(text)
        result = number / divisor
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("--- done ---")


compute("10", 4)   # Result: 2.5  --- done ---
compute("abc", 2)  # Error: ...   --- done ---
compute("10", 0)   # Error: ...   --- done ---

##############################################################################
# 5. multiple except clauses
##############################################################################

values = ["5", "0", "abc", "10", ""]

for v in values:
    try:
        print(100 / int(v))
    except ValueError:
        print(f"Cannot convert: {v!r}")
    except ZeroDivisionError:
        print("Division by zero")

# 20.0
# Division by zero
# Cannot convert: 'abc'
# 10.0
# Cannot convert: ''

##############################################################################
# 6. get_item
##############################################################################

def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None


print(get_item([10, 20, 30], 1))   # 20
print(get_item([10, 20, 30], 9))   # None

##############################################################################
# 7. safe_get
##############################################################################

def safe_get(data, key, default=None):
    try:
        return data.get(key, default)
    except (TypeError, AttributeError):
        return default


config = {"host": "localhost", "port": 8080}
print(safe_get(config, "host"))          # localhost
print(safe_get(config, "timeout", 30))   # 30
print(safe_get(None, "host", "n/a"))     # n/a

##############################################################################
# 8. validate_score
##############################################################################

def validate_score(score):
    if not isinstance(score, int):
        raise TypeError(f"Score must be int, got {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"Score {score} is out of range [0, 100]")
    return score


print(validate_score(85))   # 85
try:
    validate_score(-5)
except ValueError as e:
    print(e)                # Score -5 is out of range [0, 100]
try:
    validate_score('A')
except TypeError as e:
    print(e)                # Score must be int, got str

##############################################################################
# 9. to_upper
##############################################################################

def to_upper(text):
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    return text.upper()


print(to_upper('hello'))   # HELLO
try:
    to_upper(42)
except TypeError as e:
    print(e)               # Expected str, got int

##############################################################################
# 10. BankAccount
##############################################################################

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )
        self.balance -= amount
        return self.balance


account = BankAccount(100)
print(account.withdraw(30))   # 70
try:
    account.withdraw(200)
except ValueError as e:
    print(e)                  # Insufficient funds: ...

##############################################################################
# 11. bare raise (re-raise)
##############################################################################

def safe_parse(text):
    try:
        return int(text)
    except ValueError:
        print(f"Logging: could not parse {text!r}")
        raise


print(safe_parse("42"))   # 42
try:
    safe_parse("abc")     # Logging: could not parse 'abc'
except ValueError as e:
    print(f"Caught: {e}")

##############################################################################
# 12. NegativeValueError
##############################################################################

class NegativeValueError(Exception):
    pass


def square_root(n):
    if n < 0:
        raise NegativeValueError(f"Cannot compute square root of {n}")
    return math.sqrt(n)


print(square_root(9))   # 3.0
try:
    square_root(-4)
except NegativeValueError as e:
    print(e)            # Cannot compute square root of -4

##############################################################################
# 13. AgeError with attribute
##############################################################################

class AgeError(ValueError):
    def __init__(self, message, age):
        super().__init__(message)
        self.age = age


def check_age(age):
    if age < 18:
        raise AgeError("Must be 18 or older", age)
    return "Access granted"


try:
    print(check_age(15))
except AgeError as e:
    print(e)        # Must be 18 or older
    print(e.age)    # 15

##############################################################################
# 14. Exception hierarchy
##############################################################################

class StorageError(Exception):
    pass

class FileReadError(StorageError):
    pass

class FileWriteError(StorageError):
    pass


def read_config(path):
    raise FileReadError(f"Cannot read: {path}")


# Catch specific:
try:
    read_config("config.json")
except FileReadError as e:
    print(f"FileReadError: {e}")

# Catch via base class:
try:
    read_config("config.json")
except StorageError as e:
    print(f"StorageError: {e}")

##############################################################################
# 15. ApiError with __str__
##############################################################################

class ApiError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        return f"[{self.status_code}] {super().__str__()}"


try:
    raise ApiError("Not Found", status_code=404)
except ApiError as e:
    print(e)              # [404] Not Found
    print(e.status_code)  # 404

##############################################################################
# 16. Payment hierarchy with attribute
##############################################################################

class PaymentError(Exception):
    def __init__(self, message, amount):
        super().__init__(message)
        self.amount = amount


class InsufficientFundsError(PaymentError):
    pass


class CardDeclinedError(PaymentError):
    pass


def process_payment(amount, method):
    if method == "empty":
        raise InsufficientFundsError("Not enough funds", amount)
    if method == "blocked":
        raise CardDeclinedError("Card blocked", amount)


for method in ["empty", "blocked"]:
    try:
        process_payment(100, method)
    except PaymentError as e:
        print(f"{type(e).__name__}: {e} (amount={e.amount})")

# InsufficientFundsError: Not enough funds (amount=100)
# CardDeclinedError: Card blocked (amount=100)
