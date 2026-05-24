# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję greet(name, greeting="Hello"), która zwraca napis w formacie
# "{greeting}, {name}!". Parametr greeting ma wartość domyślną "Hello".
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", "Hi") == "Hi, Bob!"
    assert greet("Eve", greeting="Hey") == "Hey, Eve!"

test_greet()
