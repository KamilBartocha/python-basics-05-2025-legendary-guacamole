# 04 Python intermediate - Wirtualne środowisko i Debugger
# Solutions

# =============================================================================
# SECTION 1: venv
# =============================================================================

# Ćw. 1: Polecenia terminala
# Tworzenie:
# python -m venv myenv

# Aktywacja (macOS/Linux):
# source myenv/bin/activate

# Instalacja requests:
# pip install requests

# Dezaktywacja:
# deactivate

# Ćw. 2: Dwa projekty, dwie wersje selenium
# project_old - selenium 3.141.0:
# python -m venv project_old/venv
# source project_old/venv/bin/activate
# pip install selenium==3.141.0
# deactivate

# project_new - selenium 4.18.0:
# python -m venv project_new/venv
# source project_new/venv/bin/activate
# pip install selenium==4.18.0
# deactivate

# Ćw. 3: Sprawdź aktywne środowisko
import sys

print(sys.prefix)
print(sys.executable)

in_venv = sys.prefix != sys.base_prefix
print(f"W venv: {in_venv}")

# Ćw. 4: Zawartość pliku .gitignore
gitignore_entries = [
    "myenv/",
    "__pycache__/",
    "*.pyc",
    "*.pyo",
    ".env",
]

print("\n".join(gitignore_entries))

# Ćw. 5: Kompletny przepływ pracy
# mkdir my_api && cd my_api
# python -m venv venv
# source venv/bin/activate
# pip install requests pytest
# pip freeze > requirements.txt
# deactivate

print("Przepływ pracy kompletny!")


# =============================================================================
# SECTION 2: requirements.txt
# =============================================================================

# Ćw. 6: Odpowiedzi
# Dokładna wersja (==): requests
# Wersja minimalna (>=): pytest
# Polecenie instalacji: pip install -r requirements.txt

# Ćw. 7: Lista zainstalowanych pakietów
import subprocess
result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
print(result.stdout[:500])

# Ćw. 8: Wersja pakietu przez importlib.metadata
import importlib.metadata

def get_version(package_name):
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return f"{package_name} not installed"


print(get_version("pip"))
print(get_version("requests"))
print(get_version("nonexistent-package"))

# Ćw. 9: Parsowanie requirements.txt
import re

requirements_txt = "requests==2.31.0\npytest>=7.4.0\nselenium~=4.18.0\nblack\n"

def parse_requirements(content):
    result = {}
    for line in content.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        match = re.match(r'^([A-Za-z0-9_\-\.]+)(==|>=|<=|~=|!=|>|<.+)?$', line)
        if match:
            name = match.group(1)
            specifier = line[len(name):] if len(line) > len(name) else None
            result[name] = specifier if specifier else None
    return result


packages = parse_requirements(requirements_txt)
print(packages)
# {'requests': '==2.31.0', 'pytest': '>=7.4.0', 'selenium': '~=4.18.0', 'black': None}


# =============================================================================
# SECTION 3: Debugger
# =============================================================================

# Ćw. 10: Napraw błąd - sum_to_n
# Błąd: range(n) generuje 0..n-1, brakuje n w sumie
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):   # poprawka: range(1, n+1)
        total += i
    return total


print(sum_to_n(5))   # 15

# Ćw. 11: Napraw błąd - count_vowels
# Błąd 1: count == 1 zamiast count += 1 (porównanie zamiast przypisania)
# Błąd 2: brak obsługi wielkich liter
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word.lower():   # poprawka: lower() dla case-insensitive
        if char in vowels:
            count += 1          # poprawka: += zamiast ==
    return count


print(count_vowels("hello"))   # 2
print(count_vowels("APPLE"))   # 2

# Ćw. 12: Napraw błąd - primes_up_to
# Błąd: range(2, n) nie obejmuje n, więc np. primes_up_to(11) nie zwróci 11
def primes_up_to(n):
    primes = []
    for num in range(2, n + 1):   # poprawka: n + 1 aby wliczyć n
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes


print(primes_up_to(10))   # [2, 3, 5, 7]
print(primes_up_to(11))   # [2, 3, 5, 7, 11]

# Ćw. 13: breakpoint() - odpowiedzi
# Ile razy zatrzyma się breakpoint? 3 razy (dla indeksów 0, 1, 2 - do pierwszego ujemnego)
# Jakie kolejne wartości przyjmuje 'num'? 5, 3, -2

def find_first_negative(numbers):
    for i, num in enumerate(numbers):
        # breakpoint()
        if num < 0:
            return i
    return -1

data = [5, 3, -2, 8, -1, 4]
idx = find_first_negative(data)
print(f"Pierwszy ujemny na indeksie: {idx}")   # 2

# Ćw. 14: Step Into - napraw błąd w validate()
# Błąd: validate zwraca True dla value > 0, ale 0 zwróci False (poprawnie).
# Wynik [10, 16, 4] pochodzi z danych [5, 8, 2] (tylko >0 razy 2).
# Funkcja validate() jest poprawna - filtruje liczby > 0.
# Jeśli jednak oczekujemy, że 0 też przejdzie, poprawka to: value >= 0

def validate(value):
    return value > 0   # poprawne: wyklucza 0 i ujemne

def process(numbers):
    return [n * 2 for n in numbers if validate(n)]

data = [-3, 0, 5, -1, 8, 2]
result = process(data)
print(result)   # [10, 16, 4]
