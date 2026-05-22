# 05_exercise.py — 05 Pliki i moduły
import os


# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję save_and_load(path, lines), która:
#   1. Zapisuje listę napisów `lines` do pliku (każdy napis w osobnej linii).
#   2. Wczytuje plik z powrotem i zwraca listę linii bez znaków nowej linii.
def save_and_load(path, lines):
    pass


def test_save_and_load(tmp_path):
    path = str(tmp_path / "output.txt")
    result = save_and_load(path, ["alpha", "beta", "gamma"])
    assert result == ["alpha", "beta", "gamma"]


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz funkcję count_words(path), która wczytuje plik tekstowy i zwraca
# słownik {słowo: liczba_wystąpień} (małe litery, bez interpunkcji).
# Wskazówka: użyj str.split() oraz str.strip(".,!?").
def count_words(path):
    pass


def test_count_words(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("Ala ma kota. Ala lubi kota!\n", encoding="utf-8")
    result = count_words(str(p))
    assert result["ala"] == 2
    assert result["kota"] == 2
    assert result["ma"] == 1


# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Napisz funkcję csv_summary(path), która wczytuje prosty plik CSV (bez nagłówka)
# w formacie "imię,wynik" i zwraca słownik {"top": imię, "avg": średnia_wyników}.
# Zakładaj, że wyniki są liczbami całkowitymi.
# Przykład pliku(scores.csv):
#   Anna,85
#   Bartek,92
#   Celina,78
def csv_summary(path):
    pass


def test_csv_summary(tmp_path):
    p = tmp_path / "scores.csv"
    p.write_text("Anna,85\nBartek,92\nCelina,78\n", encoding="utf-8")
    result = csv_summary(str(p))
    assert result["top"] == "Bartek"
    assert abs(result["avg"] - 85.0) < 0.01
