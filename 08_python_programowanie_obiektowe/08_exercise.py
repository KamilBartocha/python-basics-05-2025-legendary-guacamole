# 08_exercise.py — 008 Programowanie obiektowe

# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz hierarchię klas do reprezentacji figur geometrycznych:
#   Shape  (klasa bazowa) — metoda area() zwraca 0
#   Circle(radius)        — pole = π * r²  (użyj math.pi)
#   Rectangle(width, height) — pole = width * height
#   Triangle(base, height)   — pole = 0.5 * base * height
# Każda klasa powinna mieć metodę __repr__ zwracającą czytelny opis.
import math


class Shape:
    pass


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


class Triangle(Shape):
    pass


def test_shapes():
    assert Shape().area() == 0

    c = Circle(5)
    assert abs(c.area() - math.pi * 25) < 1e-9

    r = Rectangle(4, 6)
    assert r.area() == 24

    t = Triangle(3, 8)
    assert t.area() == 12.0

    assert isinstance(c, Shape)
    assert isinstance(r, Shape)
    assert isinstance(t, Shape)


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz klasę BankAccount z:
#   __init__(owner, balance=0)
#   deposit(amount)   — dodaje środki; zgłasza ValueError gdy amount <= 0
#   withdraw(amount)  — odejmuje środki; zgłasza ValueError gdy amount <= 0
#                       lub gdy środków jest za mało (komunikat: "Niewystarczające środki")
#   transfer(amount, target_account) — przelewa środki z self na target_account
#   __repr__          — np. "BankAccount(owner='Jan', balance=100)"
class BankAccount:
    pass


def test_bank_account():
    alice = BankAccount("Alice", 100)
    bob = BankAccount("Bob")

    alice.deposit(50)
    assert alice.balance == 150

    alice.withdraw(30)
    assert alice.balance == 120

    alice.transfer(40, bob)
    assert alice.balance == 80
    assert bob.balance == 40

    try:
        alice.withdraw(1000)
        assert False, "Powinien być ValueError"
    except ValueError as e:
        assert "środki" in str(e).lower() or "niewystarczające" in str(e).lower()

    try:
        alice.deposit(-10)
        assert False, "Powinien być ValueError"
    except ValueError:
        pass
