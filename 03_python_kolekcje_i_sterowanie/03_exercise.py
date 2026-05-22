# 03_exercise.py — 003 Kolekcje i sterowanie

# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Operacje na liście i słowniku.
# Dane: lista ocen studenta.
# Zadanie:
#   - oblicz średnią ocen
#   - znajdź ocenę minimalną i maksymalną
#   - zbuduj słownik {"min": ..., "max": ..., "avg": ...}
#   - wypisz wyniki sformatowane do 2 miejsc po przecinku
grades = [4, 3, 5, 2, 4, 5, 3, 4]


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Instrukcje warunkowe i pętla.
# Dane: lista liczb całkowitych.
# Zadanie:
#   - wypisz każdą liczbę i opisz ją: "parzysta" / "nieparzysta"
#   - policz ile liczb jest parzystych, ile nieparzystych
#   - wypisz podsumowanie: "Parzyste: X, Nieparzyste: Y"
numbers = [7, 2, 15, 8, 3, 10, 1, 6]


# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Zbiory i krotki.
# Dane: dwie listy słów (mogą zawierać duplikaty).
# Zadanie:
#   - znajdź słowa wspólne dla obu list (część wspólna zbiorów)
#   - znajdź słowa unikalne dla każdej listy (różnica zbiorów)
#   - wypisz wyniki w postaci posortowanej krotki
words_a = ["pies", "kot", "ryba", "ptak", "pies", "kot"]
words_b = ["kot", "ryba", "żółw", "kot", "chomik"]


# ─── Ćwiczenie 4 ──────────────────────────────────────────────────────────────
# Konwersja dwóch list na słownik używając pętli.
# Dane: listy kluczy i wartości tej samej długości.
# Zadanie:
#   - zbuduj słownik iterując jednocześnie po obu listach
#   - wypisz wynik
# Oczekiwany wynik: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys   = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


# ─── Ćwiczenie 5 ──────────────────────────────────────────────────────────────
# Iteracja po słowniku z .items().
# Dane: słownik studenta.
# Zadanie:
#   - wydrukuj wartość klucza 'name'
#   - dodaj klucz 'passed' z wartością True
#   - wydrukuj wszystkie pary klucz-wartość używając .items()
student = {'name': 'Alice', 'grade': 'B', 'age': 20}


# ─── Ćwiczenie 6 ──────────────────────────────────────────────────────────────
# Zliczanie częstości słów za pomocą słownika. *(Trudniejsze)*
# Dane: lista słów (z powtórzeniami).
# Zadanie:
#   - zbuduj słownik {słowo: liczba_wystąpień} używając pętli i operatora in
#   - wypisz wynik
# Oczekiwany wynik: {'apple': 3, 'banana': 2, 'cherry': 1}
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
freq = {}

print(freq)


# ─── Ćwiczenie 7 — FizzBuzz ───────────────────────────────────────────────────
# Klasyczne pytanie rekrutacyjne.
# Zadanie: dla liczb od 1 do 20 wypisz:
#   - 'FizzBuzz' jeśli liczba jest podzielna przez 3 i 5
#   - 'Fizz'     jeśli podzielna przez 3
#   - 'Buzz'     jeśli podzielna przez 5
#   - samą liczbę w pozostałych przypadkach
# Przykład: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...



# ─── Ćwiczenie 8 — Two Sum ────────────────────────────────────────────────────
# Klasyczne pytanie rekrutacyjne.
# Dane: lista liczb i wartość docelowa (target).
# Zadanie: znajdź dwie liczby z listy, które sumują się do target.
#   - zwróć je jako krotkę (tuple), mniejsza liczba pierwsza
#   - zakładamy, że dokładnie jedna para istnieje
# Oczekiwany wynik: (2, 7)
# hint: użyj zagnieżdżonej pętli for (najprostsze podejście, ale nie optymalne)
numbers = [2, 7, 11, 15]
target = 9
result = ...
print(result)   # (2, 7)


# ─── Ćwiczenie 9 — Palindrom ──────────────────────────────────────────────────
# Klasyczne pytanie rekrutacyjne.
# Dane: słowo (może zawierać duże i małe litery).
# Zadanie: sprawdź czy słowo jest palindromem (czyta się tak samo
#   od przodu i od tyłu). Ignoruj wielkość liter.
# Oczekiwany wynik: True
word_1 = 'Racecar'
word_2 = "Alamakota"
word_3 = "Rower"
