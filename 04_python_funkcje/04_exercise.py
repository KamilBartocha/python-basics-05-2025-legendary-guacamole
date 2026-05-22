# 04_exercise.py — 004 Funkcje


# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję greet(name, greeting="Hello"), która zwraca napis w formacie
# "{greeting}, {name}!". Parametr greeting ma wartość domyślną "Hello".
def greet(name, greeting="Hello"):
    pass


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", "Hi") == "Hi, Bob!"
    assert greet("Eve", greeting="Hey") == "Hey, Eve!"


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz funkcję calculate_bmi(weight, height) obliczającą wskaźnik BMI.
# Wzor: BMI = weight / height**2, zaokrąglony do 1 miejsca po przecinku.
# Dodaj docstring opisujący co robi funkcja i jakie przyjmuje parametry.
# Sprawdź docstring przez help(calculate_bmi) lub calculate_bmi.__doc__.
def calculate_bmi(weight, height):
    """..."""
    pass


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.9
    assert calculate_bmi(90, 1.80) == 27.8
    assert calculate_bmi.__doc__ is not None
    assert len(calculate_bmi.__doc__.strip()) > 5


# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Napisz funkcję total(*args), która zwraca sumę wszystkich przekazanych liczb.
# Powinna działać dla dowolnej liczby argumentów (0 lub więcej).
def total(*args):
    pass


def test_total():
    assert total(1, 2, 3) == 6
    assert total(10, 20) == 30
    assert total(5) == 5
    assert total() == 0


# ─── Ćwiczenie 4 ──────────────────────────────────────────────────────────────
# Napisz funkcję build_profile(**kwargs), która zwraca słownik z przekazanymi
# danymi, zawsze dodając klucz 'active': True.
# Przykład: build_profile(name='Alice', age=30)
#        -> {'name': 'Alice', 'age': 30, 'active': True}
def build_profile(**kwargs):
    pass


def test_build_profile():
    result = build_profile(name="Alice", age=30)
    assert result == {"name": "Alice", "age": 30, "active": True}

    result = build_profile()
    assert result == {"active": True}

    result = build_profile(city="Warsaw")
    assert result["active"] is True
    assert result["city"] == "Warsaw"


# ─── Ćwiczenie 5 ──────────────────────────────────────────────────────────────
# Napisz funkcję fizz_buzz(n), która zwraca listę napisów dla liczb 1..n:
#   - "FizzBuzz" jeśli liczba dzieli się przez 3 i przez 5
#   - "Fizz"     jeśli dzieli się tylko przez 3
#   - "Buzz"     jeśli dzieli się tylko przez 5
#   - str(liczba) w pozostałych przypadkach
def fizz_buzz(n):
    pass


def test_fizz_buzz():
    assert fizz_buzz(1) == ["1"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15)[-1] == "FizzBuzz"
    assert fizz_buzz(0) == []


# ─── Ćwiczenie 6 ──────────────────────────────────────────────────────────────
# Napisz funkcję make_adder(n), która zwraca funkcję wewnętrzną add(x).
# Zwrócona funkcja add(x) zwraca x + n (używa n z zakresu zewnętrznego).
# Przykład:
#   add5 = make_adder(5)
#   add5(3)  ->  8
#   add5(10) -> 15
def make_adder(n):
    pass


def test_make_adder():
    add5 = make_adder(5)
    assert add5(3) == 8
    assert add5(10) == 15

    add0 = make_adder(0)
    assert add0(7) == 7


# ─── Ćwiczenie 7 ──────────────────────────────────────────────────────────────
# Napisz funkcję make_counter(start=0), która zwraca funkcję wewnętrzną.
# Każde wywołanie zwróconej funkcji zwiększa licznik o 1 i zwraca jego wartość.
# Przykład:
#   counter = make_counter(10)
#   counter()  ->  11
#   counter()  ->  12
def make_counter(start=0):
    pass


def test_make_counter():
    c = make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3

    c2 = make_counter(10)
    assert c2() == 11
    assert c2() == 12


# ─── Ćwiczenie 8 ──────────────────────────────────────────────────────────────
# Napisz funkcję flatten_shallow(nested), która spłaszcza listę zagnieżdżoną
# o 2 poziomach głębokości do jednej płaskiej listy.
# Przykład: flatten_shallow([1, [2, 4], 5, [1, 1]]) == [1, 2, 4, 5, 1, 1]
def flatten_shallow(nested):
    pass


def test_flatten_shallow():
    assert flatten_shallow([1, 2, 3]) == [1, 2, 3]
    assert flatten_shallow([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten_shallow([1, [2, 4], 5, [1, 1]]) == [1, 2, 4, 5, 1, 1]
    assert flatten_shallow([]) == []


# ─── Ćwiczenie 9 ──────────────────────────────────────────────────────────────
# Napisz funkcję flatten_deep(nested), która spłaszcza listę zagnieżdżoną
# o dowolnej głębokości do jednej płaskiej listy.
# Przykład: flatten_deep([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
# hint: użyj rekurencji
def flatten_deep(nested):
    pass


def test_flatten_deep():
    assert flatten_deep([1, 2, 3]) == [1, 2, 3]
    assert flatten_deep([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten_deep([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
    assert flatten_deep([]) == []
