# 07_exercise.py — 07 Programowanie funkcyjne


# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję pipeline(value, *funcs), która przekazuje wartość przez
# łańcuch funkcji: wynik każdej trafia jako argument do następnej.
# Przykład: pipeline(5, lambda x: x*2, lambda x: x+1) == 11
def pipeline(value, *funcs):
    pass


def test_pipeline():
    double = lambda x: x * 2
    inc = lambda x: x + 1
    square = lambda x: x ** 2

    assert pipeline(3, double) == 6
    assert pipeline(3, double, inc) == 7
    assert pipeline(3, inc, double, square) == 64
    assert pipeline(5) == 5


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz funkcję group_by(iterable, key_func), która grupuje elementy kolekcji
# według wartości zwróconej przez key_func.
# Zwraca słownik {klucz: [elementy]}.
# Przykład:
#   group_by(["cat", "car", "bar", "bat"], lambda w: w[0])
#   → {"c": ["cat", "car"], "b": ["bar", "bat"]}
def group_by(iterable, key_func):
    pass


def test_group_by():
    words = ["cat", "car", "bar", "bat"]
    result = group_by(words, lambda w: w[0])
    assert result == {"c": ["cat", "car"], "b": ["bar", "bat"]}

    nums = [1, 2, 3, 4, 5, 6]
    result2 = group_by(nums, lambda n: "even" if n % 2 == 0 else "odd")
    assert result2["even"] == [2, 4, 6]
    assert result2["odd"] == [1, 3, 5]

    assert group_by([], lambda x: x) == {}


# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Napisz funkcję memoize(func), która opakowuje funkcję jednoargumentową
# w cache (słownik). Kolejne wywołania z tym samym argumentem zwracają
# zapamiętany wynik bez ponownego wywołania oryginalnej funkcji.
def memoize(func):
    pass


def test_memoize():
    call_count = 0

    def expensive(n):
        nonlocal call_count
        call_count += 1
        return n * n

    cached = memoize(expensive)

    assert cached(4) == 16
    assert call_count == 1
    assert cached(4) == 16
    assert call_count == 1   # nie wywołano ponownie

    assert cached(5) == 25
    assert call_count == 2
