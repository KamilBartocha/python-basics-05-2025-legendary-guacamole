# 06_exercise.py — 06 Wyjątki


# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję safe_divide(a, b), która:
#   - zwraca wynik dzielenia a / b jako float
#   - zgłasza ValueError z komunikatem "Dzielnik nie może być zerem" gdy b == 0
#   - zgłasza TypeError z komunikatem "Argumenty muszą być liczbami" gdy a lub b
#     nie jest typu int ani float
def safe_divide(a, b):
    pass


def test_safe_divide():
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(0, 5) == 0.0

    try:
        safe_divide(10, 0)
        assert False, "Powinien być ValueError"
    except ValueError as e:
        assert "zerem" in str(e)

    try:
        safe_divide("10", 2)
        assert False, "Powinien być TypeError"
    except TypeError as e:
        assert "liczbami" in str(e)


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz własny wyjątek NegativeValueError (dziedziczy po ValueError).
# Następnie napisz funkcję sqrt_positive(x), która:
#   - zwraca pierwiastek kwadratowy z x (użyj x ** 0.5)
#   - zgłasza NegativeValueError gdy x < 0
class NegativeValueError(ValueError):
    pass


def sqrt_positive(x):
    pass


def test_sqrt_positive():
    assert sqrt_positive(9) == 3.0
    assert sqrt_positive(0) == 0.0

    try:
        sqrt_positive(-1)
        assert False, "Powinien być NegativeValueError"
    except NegativeValueError:
        pass