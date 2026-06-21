# Solutions: 05_python_interm_own_modules.ipynb
##############################################################################
# 1. mathutils functions
##############################################################################

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def average(*args):
    return sum(args) / len(args)


print(add(3, 4))            # 7
print(subtract(10, 3))      # 7
print(multiply(3, 4))       # 12
print(average(1, 2, 3, 4))  # 2.5

##############################################################################
# 2. stringutils functions
##############################################################################

def clean(text):
    return text.strip()


def capitalize_words(text):
    return text.title()


def count_words(text):
    return len(text.split())


print(clean("  hello world  "))         # hello world
print(capitalize_words("hello world"))  # Hello World
print(count_words("one two three"))     # 3

##############################################################################
# 3. __init__.py dla pakietu myutils (strukturalne - jako komentarze)
##############################################################################

# myutils/__init__.py:
#
# from .mathutils import add, subtract, multiply, average
# from .stringutils import clean, capitalize_words, count_words
#
# Użytkownik importuje:
# from myutils import add, clean

##############################################################################
# 4. Różne style importu
##############################################################################

# a) import całego modułu
import math
print(math.ceil(3.2))   # 4

# b) import konkretnej funkcji
from math import floor
print(floor(3.8))       # 3

# c) import z aliasem
from math import pow as power
print(power(2, 10))     # 1024.0

##############################################################################
# 5. calculator/__init__.py (strukturalne - jako komentarze)
##############################################################################

# calculator/__init__.py:
#
# from .basic_ops import add, subtract, multiply
# from .advanced_ops import power, sqrt
#
# Użytkownik importuje:
# from calculator import add, subtract, multiply

##############################################################################
# 6. SimpleJSON
##############################################################################

import json


class SimpleJSON:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load(self):
        try:
            with open(self.file_path) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")

    def get(self, key):
        return self.data.get(key) if self.data else None


class SimpleJSONFromString(SimpleJSON):
    """Wersja testowa - wczytuje z napisu zamiast pliku."""
    def __init__(self, json_string):
        self.data = json.loads(json_string)
        self.file_path = None

    def load(self):
        pass


sample = '{"name": "Alice", "age": 30, "city": "Warsaw"}'
reader = SimpleJSONFromString(sample)
print(reader.get("name"))   # Alice
print(reader.get("age"))    # 30

##############################################################################
# 7. SimpleJSONExtended z keys() i summary()
##############################################################################

class SimpleJSONExtended(SimpleJSONFromString):
    def keys(self):
        return list(self.data.keys())

    def summary(self):
        for key, val in self.data.items():
            print(f"{key}: {type(val).__name__}")


sample2 = '{"name": "Alice", "age": 30, "scores": [95, 87]}'
reader2 = SimpleJSONExtended(sample2)
print(reader2.keys())   # ['name', 'age', 'scores']
reader2.summary()
# name: str
# age: int
# scores: list

##############################################################################
# 8. Struktura biblioteki csvreader
##############################################################################

structure = """
csvreader/
├── csvreader/
│   ├── __init__.py
│   └── csv_reader.py
├── tests/
│   ├── example1.csv
│   └── test_csv_reader.py
├── README.md
└── setup.py
"""

print(structure)

##############################################################################
# 9. get_nested - nawigacja po zagnieżdżonym słowniku
##############################################################################

data = {
    'user': {
        'name': 'Alice',
        'scores': [95, 87, 92]
    }
}

def get_nested(data, path):
    current = data
    for part in path.split('.'):
        if current is None:
            return None
        if '[' in part:
            key = part[:part.index('[')]
            index = int(part[part.index('[') + 1:part.index(']')])
            current = current.get(key) if isinstance(current, dict) else None
            if isinstance(current, list):
                current = current[index] if index < len(current) else None
        else:
            current = current.get(part) if isinstance(current, dict) else None
    return current


print(get_nested(data, 'user.name'))        # Alice
print(get_nested(data, 'user.scores[0]'))   # 95
print(get_nested(data, 'missing.key'))      # None

##############################################################################
# 10. Testy unittest dla mathutils
##############################################################################

import unittest


class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_average(self):
        self.assertEqual(average(1, 2, 3, 4), 2.5)
        self.assertEqual(average(10, 20), 15.0)


##############################################################################
# 11. Test obsługi błędu FileNotFoundError w ReadJSON
##############################################################################

import sys
sys.path.insert(0, '05_library/datareader')
from datareader.json_reader import ReadJSON


class TestReadJSONErrors(unittest.TestCase):
    def test_file_not_found(self):
        reader = ReadJSON('nonexistent_path.json')
        reader.load_json()
        self.assertIsNone(reader.data)


##############################################################################
# 12. setup.py dla myutils (strukturalne - jako komentarze)
##############################################################################

# from setuptools import setup, find_packages
#
# setup(
#     name='myutils',
#     version='1.0.0',
#     description='Math and string utility functions',
#     packages=find_packages(),
#     python_requires='>=3.8',
# )
#
# Instalacja lokalna:
# pip install .
# pip install -e .   # tryb edytowalny (editable mode)

##############################################################################
# 13. Testy sprawdzające wyjątki (assertRaises)
##############################################################################

def divide(a, b):
    return a / b


class TestExceptions(unittest.TestCase):
    def test_average_no_args(self):
        self.assertRaises(ZeroDivisionError, average)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)


unittest.main(argv=[''], exit=False, verbosity=2)
