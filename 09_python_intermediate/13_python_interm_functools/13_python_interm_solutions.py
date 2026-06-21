"""13 Python intermediate - functools - rozwiązania."""
from functools import partial, lru_cache, cache, reduce, total_ordering, wraps
from datetime import datetime
import time


# ---------------------------------------------------------------------------
# Ćw. 1: partial - greet
# ---------------------------------------------------------------------------
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


greet_pl = partial(greet, greeting="Cześć")
print(greet("Alice"))
print(greet_pl("Alice"))


# ---------------------------------------------------------------------------
# Ćw. 2: partial - log
# ---------------------------------------------------------------------------
def log(level: str, message: str, timestamp: bool = True) -> str:
    ts = f"[{datetime.now():%H:%M:%S}] " if timestamp else ""
    return f"{ts}[{level}] {message}"


log_info  = partial(log, "INFO",  timestamp=False)
log_error = partial(log, "ERROR", timestamp=False)

print(log_info("Server started"))
print(log_error("Connection refused"))


# ---------------------------------------------------------------------------
# Ćw. 3: partial + map - set_field
# ---------------------------------------------------------------------------
def set_field(d: dict, key: str, value) -> dict:
    return {**d, key: value}


users = [
    {"name": "Alice", "active": False},
    {"name": "Bob",   "active": False},
]
activate = partial(set_field, key="active", value=True)
result = list(map(activate, users))
print(result)


# ---------------------------------------------------------------------------
# Ćw. 4: lru_cache - count_ways
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def count_ways(n: int) -> int:
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return count_ways(n - 1) + count_ways(n - 2)


for i in range(1, 8):
    print(f"count_ways({i}) = {count_ways(i)}")


# ---------------------------------------------------------------------------
# Ćw. 5: lru_cache - expensive_computation
# ---------------------------------------------------------------------------
@lru_cache(maxsize=128)
def expensive_computation(x: int, y: int) -> int:
    time.sleep(0.1)
    return x * y + x - y


t0 = time.perf_counter()
print(expensive_computation(10, 20))
print(f"first call:  {time.perf_counter()-t0:.4f}s")

t0 = time.perf_counter()
print(expensive_computation(10, 20))
print(f"second call: {time.perf_counter()-t0:.4f}s")


# ---------------------------------------------------------------------------
# Ćw. 6: własny memoize
# ---------------------------------------------------------------------------
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(30))   # 832040


# ---------------------------------------------------------------------------
# Ćw. 7: @cache + cache_info
# ---------------------------------------------------------------------------
@cache
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


for i in range(1, 8):
    print(f"{i}! = {factorial(i)}")

print(factorial.cache_info())


# ---------------------------------------------------------------------------
# Ćw. 8: reduce - max i suma kwadratów
# ---------------------------------------------------------------------------
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(f"max: {maximum}")   # 9

sum_of_squares = reduce(lambda acc, x: acc + x * x, numbers, 0)
print(f"sum of squares: {sum_of_squares}")   # 173


# ---------------------------------------------------------------------------
# Ćw. 9: reduce - scalanie słowników
# ---------------------------------------------------------------------------
dicts = [{"a": 1}, {"b": 2}, {"c": 3}]
merged = reduce(lambda acc, d: {**acc, **d}, dicts, {})
print(merged)   # {'a': 1, 'b': 2, 'c': 3}


# ---------------------------------------------------------------------------
# Ćw. 10: total_ordering - Card
# ---------------------------------------------------------------------------
@total_ordering
class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
             9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}

    def __init__(self, suit: str, rank: int):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other) -> bool:
        return self.rank == other.rank

    def __lt__(self, other) -> bool:
        return self.rank < other.rank

    def __repr__(self) -> str:
        return f"{self.RANKS[self.rank]}{self.suit}"


hand = [Card("♠", 10), Card("♥", 14), Card("♣", 5), Card("♦", 10)]
print(sorted(hand))


# ---------------------------------------------------------------------------
# Ćw. 11: functools.wraps - dekorator timer
# ---------------------------------------------------------------------------
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-t0:.4f}s")
        return result
    return wrapper


@timer
def slow_add(a: int, b: int) -> int:
    """Dodaje dwie liczby z opóźnieniem."""
    time.sleep(0.05)
    return a + b


result = slow_add(3, 4)
print(result)              # 7
print(slow_add.__name__)   # slow_add
print(slow_add.__doc__)    # Dodaje dwie liczby z opóźnieniem.
