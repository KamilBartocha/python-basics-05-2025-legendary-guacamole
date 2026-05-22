# Python od podstaw - Syllabus

## Moduł 01 - Instalacja i środowiska

1. Python - instalacja (Windows / macOS), weryfikacja
2. Edytor kodu vs. IDE
3. PyCharm Community
4. Visual Studio Code + wtyczki (Python, Pylance, Jupyter, Git)
5. IDLE
6. Algorytm - definicja, cechy, pseudokod
7. Schemat blokowy (flowchart) - symbole i przepływ
8. Pierwsze programy: `print()`, zmienne, f-stringi
9. Jupyter Notebook - komórki kodu i markdown
10. Git - podstawy kontroli wersji

---

## Moduł 02 - Składnia i typy proste

1. `print()` - konkatenacja, `str.format()`, f-stringi
2. Komentarze (`#`, wieloliniowe)
3. Zmienne i typy danych: `int`, `float`, `bool`, `str`, `list`, `dict`
4. Operatory arytmetyczne: `+`, `-`, `*`, `/`, `//`, `%`, `**`
5. Operatory porównania i logiczne: `==`, `!=`, `>`, `<`, `not`, `and`, `or`
6. Typ `bool`, `None`, konwersja typów: `int()`, `float()`, `str()`, `bool()`
7. `isinstance()`
8. Ciągi znaków (string) - indeksowanie, slicing, metody: `upper()`, `lower()`, `replace()`, `split()`, `strip()`
9. Wejście od użytkownika - `input()`

---

## Moduł 03 - Kolekcje i sterowanie

1. Lista (`list`) - tworzenie, indeksowanie, slicing, metody: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `sorted()`
2. Krotka (`tuple`) - niemutowalność, indeksowanie
3. Słownik (`dict`) - pary klucz-wartość, metody: `keys()`, `values()`, `items()`, operator `in`
4. Zbiór (`set`) - unikalność, operacje: `|`, `&`, `-`, `^`, metody: `add()`, `update()`, `remove()`
5. Instrukcje warunkowe: `if` / `elif` / `else`, wyrażenie warunkowe (ternary)
6. Pętla `for` - iteracja, `range()`, `enumerate()`
7. Pętla `while`
8. `break`, `continue`, `pass`
9. Pętle zagnieżdżone

---

## Moduł 04 - Funkcje

1. Definiowanie funkcji (`def`), konwencje nazewnictwa
2. Parametry i argumenty - pozycyjne, domyślne
3. Zwracanie wartości (`return`)
4. Zasięg zmiennych - reguła LEGB (Local, Enclosing, Global, Built-in)
5. Słowo kluczowe `global`
6. Docstringi, `help()`
7. Rekurencja - przypadek bazowy, silnia, Fibonacci
8. `*args` i `**kwargs`

---

## Moduł 05 - Pliki i moduły

1. Otwieranie plików - `open()`, tryby: `'r'`, `'w'`, `'a'`
2. Odczyt: `read()`, `readline()`, `readlines()`, iteracja pętlą
3. Zapis: `write()`, tryb nadpisania vs. dołączania
4. Menedżer kontekstu (`with open() as f:`)
5. Moduły - `import`, `import as`, `from ... import`
6. Biblioteka standardowa: `math`, `os`, `sys`, `time`
7. Instalacja pakietów - `pip`, PyPI, `pip install`, `pip freeze`
8. Środowiska wirtualne (`venv`) - tworzenie, aktywacja, `requirements.txt`
9. `if __name__ == '__main__'`

---

## Moduł 06 - Wyjątki

1. Czym jest wyjątek - traceback, mechanizm
2. Wbudowane wyjątki: `ZeroDivisionError`, `NameError`, `TypeError`, `ValueError`, `IndexError`, `KeyError`, `FileNotFoundError`, `AttributeError`
3. Obsługa wyjątków: `try` / `except` / `else` / `finally`
4. Przechwytywanie wielu typów wyjątków, bindowanie (`as`)
5. Rzucanie wyjątków - `raise`
6. Własne klasy wyjątków - dziedziczenie po `Exception`

---

## Moduł 07 - Programowanie funkcyjne

1. Paradygmat funkcyjny vs. imperatywny
2. Czyste funkcje (pure functions), efekty uboczne, niemutowalność
3. Funkcje wyższego rzędu (first-class functions)
4. Funkcje lambda (`lambda x: wyrażenie`)
5. List comprehension - składnia, filtrowanie, zagnieżdżanie
6. Set comprehension
7. Dict comprehension, `zip()`
8. `map()` i `filter()`
9. `reduce()` z `functools`
10. Wyrażenia generatorowe - leniwa ewaluacja, efektywność pamięciowa
11. `any()` i `all()`

---

## Moduł 08 - Programowanie obiektowe

1. Czym jest OOP - obiekty, klasy, paradygmat
2. Wszystko jest obiektem - `type()`, `isinstance()`, tożsamość vs. wartość
3. Tożsamość (`id`), typ, wartość - operator `is` vs. `==`
4. Atrybuty i metody - notacja kropkowa
5. Funkcje vs. metody, parametr `self`
6. Tworzenie własnych klas - `class`, `__init__`, atrybuty instancji
7. Metody specjalne (dunder): `__str__`, `__repr__`, `__len__`
8. Cztery filary OOP: enkapsulacja, abstrakcja, dziedziczenie, polimorfizm
9. Dziedziczenie - klasa bazowa i pochodna, `super()`, nadpisywanie metod
10. Hierarchia klas, `isinstance()` z dziedziczeniem
