"""12 Python intermediate - Generatory i iteratory - rozwiązania."""
import itertools
from collections import deque


# ---------------------------------------------------------------------------
# Ćw. 1: Range_
# ---------------------------------------------------------------------------
class Range_:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self) -> int:
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


print(list(Range_(1, 10, 2)))    # [1, 3, 5, 7, 9]
print(list(Range_(0, 6)))        # [0, 1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# Ćw. 2: Fibonacci
# ---------------------------------------------------------------------------
class Fibonacci:
    def __init__(self, limit: int):
        self.limit = limit
        self.a, self.b = 1, 1

    def __iter__(self):
        self.a, self.b = 1, 1
        return self

    def __next__(self) -> int:
        if self.a > self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


print(list(Fibonacci(00)))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# ---------------------------------------------------------------------------
# Ćw. 3: Cycle
# ---------------------------------------------------------------------------
class Cycle:
    def __init__(self, sequence):
        self.sequence = list(sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence:
            raise StopIteration
        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value


c = Cycle([1, 2, 3])
result = [next(c) for _ in range(10)]
print(result)   # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]


# ---------------------------------------------------------------------------
# Ćw. 4: evens
# ---------------------------------------------------------------------------
def evens(n: int):
    for i in range(0, n + 1, 2):
        yield i


print(list(evens(10)))   # [0, 2, 4, 6, 8, 10]


# ---------------------------------------------------------------------------
# Ćw. 5: running_average
# ---------------------------------------------------------------------------
def running_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
        yield total / count


print(list(running_average([1, 3, 5, 7])))   # [1.0, 2.0, 3.0, 4.0]


# ---------------------------------------------------------------------------
# Ćw. 6: flatten
# ---------------------------------------------------------------------------
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print(list(flatten([1, [2, [3, 4]], 5])))        # [1, 2, 3, 4, 5]
print(list(flatten([[1, 2], [3, [4, [5]]]])))     # [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# Ćw. 7: generator expressions
# ---------------------------------------------------------------------------
words = ['apple', 'kiwi', 'banana', 'fig', 'cherry', 'plum']

squares_gen = (x ** 2 for x in range(0, 21, 2))
print(list(squares_gen))   # [0, 4, 16, 36, 64, 100]

long_words_gen = (w for w in words if len(w) > 4)
print(list(long_words_gen))   # ['apple', 'banana', 'cherry']


# ---------------------------------------------------------------------------
# Ćw. 8: tree_values
# ---------------------------------------------------------------------------
def tree_values(node: dict):
    yield node["value"]
    for child in node.get("children", []):
        yield from tree_values(child)


tree = {
    "value": 1,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": [
            {"value": 4, "children": []}
        ]},
    ],
}
print(list(tree_values(tree)))   # [1, 2, 3, 4]


# ---------------------------------------------------------------------------
# Ćw. 9: interleave
# ---------------------------------------------------------------------------
def interleave(*iters):
    iterators = [iter(it) for it in iters]
    while iterators:
        next_iterators = []
        for it in iterators:
            try:
                yield next(it)
                next_iterators.append(it)
            except StopIteration:
                pass
        iterators = next_iterators


print(list(interleave([1, 2, 3], ["a", "b", "c"])))
# [1, 'a', 2, 'b', 3, 'c']


# ---------------------------------------------------------------------------
# Ćw. 10: moving_window
# ---------------------------------------------------------------------------
def moving_window(iterable, size: int):
    window = deque(maxlen=size)
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield tuple(window)


print(list(moving_window([1, 2, 3, 4, 5], 3)))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]


# ---------------------------------------------------------------------------
# Ćw. 11: running_sum z send()
# ---------------------------------------------------------------------------
def running_sum():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


gen = running_sum()
next(gen)
print(gen.send(10))    # 10
print(gen.send(5))     # 15
print(gen.send(-3))    # 12
gen.close()


# ---------------------------------------------------------------------------
# Ćw. 12: countdown z throw() i close()
# ---------------------------------------------------------------------------
def countdown(n: int):
    current = n
    while True:
        try:
            yield current
            current -= 1
            if current < 0:
                return
        except ValueError:
            print("Reset!")
            current = n


gen = countdown(5)
print(next(gen))                    # 5
print(next(gen))                    # 4
gen.throw(ValueError, "reset!")     # Reset!
print(next(gen))                    # 5
gen.close()


# ---------------------------------------------------------------------------
# Ćw. 13: chain.from_iterable + compress
# ---------------------------------------------------------------------------
nested = [[1, 2], [3], [4, 5, 6]]
flat = list(itertools.chain.from_iterable(nested))
print(flat)   # [1, 2, 3, 4, 5, 6]

mask = [i % 2 == 0 for i in range(len(flat))]
print(list(itertools.compress(flat, mask)))   # [1, 3, 5]


# ---------------------------------------------------------------------------
# Ćw. 14: combinations + permutations
# ---------------------------------------------------------------------------
letters = ["a", "b", "c", "d"]
combos = list(itertools.combinations(letters, 3))
print(combos)
print(f"Combinations: {len(combos)}")   # 4

perms = list(itertools.permutations(letters, 2))
print(perms)


# ---------------------------------------------------------------------------
# Ćw. 15: groupby - sumy transakcji
# ---------------------------------------------------------------------------
transactions = [
    ("Alice", 00), ("Bob", 50),
    ("Alice", 200), ("Bob", 75),
]
sorted_tx = sorted(transactions, key=lambda x: x[0])
totals = {
    name: sum(v for _, v in group)
    for name, group in itertools.groupby(sorted_tx, key=lambda x: x[0])
}
print(totals)   # {'Alice': 300, 'Bob': 125}


# ---------------------------------------------------------------------------
# Ćw. 16: count + cycle + islice
# ---------------------------------------------------------------------------
result_a = list(itertools.islice(itertools.count(10, 3), 9))
print(result_a)   # [10, 13, 16, 19, 22, 25, 28, 31, 34]

result_b = list(itertools.islice(itertools.cycle(['A', 'B', 'C']), 9))
print(result_b)   # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']


# ---------------------------------------------------------------------------
# Ćw. 17: repeat + product
# ---------------------------------------------------------------------------
zeros = itertools.repeat(0, 5)
print(list(zeros))   # [0, 0, 0, 0, 0]

pins = list(itertools.product(range(4), repeat=2))
pin_strings = [f'{a}{b}' for a, b in pins]
print(pin_strings)
print(f'Total: {len(pin_strings)}')   # Total: 16
