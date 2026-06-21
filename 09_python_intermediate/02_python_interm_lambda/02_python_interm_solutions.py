# Solutions: 02_python_interm_lambda_map_filter_comp.ipynb
##############################################################################
# 1. List comprehensions - trzy listy
##############################################################################

squares   = [x**2 for x in range(1, 11)]
evens     = [x for x in range(21) if x % 2 == 0]
uppercase = [c.upper() for c in ['a', 'b', 'c', 'd']]

print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 00]
print(evens)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(uppercase)  # ['A', 'B', 'C', 'D']

##############################################################################
# 2. List comprehension - filtrowanie i transformacja
##############################################################################

words  = ["apple", "banana", "cherry", "date", "fig"]
result = [w.upper() for w in words if len(w) > 4]

print(result)  # ['APPLE', 'BANANA', 'CHERRY']

##############################################################################
# 3. Tuply (liczba, kwadrat, szescian) dla nieparzystych
##############################################################################

result = [(x, x**2, x**3) for x in range(1, 11) if x % 2 != 0]

print(result)
# [(1, 1, 1), (3, 9, 27), (5, 25, 125), (7, 49, 343), (9, 81, 729)]

##############################################################################
# 4. Zagnieżdżone list comprehension - tabliczka mnożenia
##############################################################################

multiplication = [(i, j, i * j) for i in range(1, 4) for j in range(1, 4)]

print(multiplication)
# [(1, 1, 1), (1, 2, 2), (1, 3, 3), (2, 1, 2), (2, 2, 4),
#  (2, 3, 6), (3, 1, 3), (3, 2, 6), (3, 3, 9)]

##############################################################################
# 5. Dictionary comprehension - dlugosc imion
##############################################################################

names        = ['Alice', 'Bob', 'Charlie', 'Diana']
name_lengths = {name: len(name) for name in names}

print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'Diana': 5}

##############################################################################
# 6. Dictionary comprehension - filtrowanie i zaokraglanie cen
##############################################################################

prices    = {'apple': 1.5, 'banana': 0.5, 'cherry': 3.0, 'date': 2.5}
expensive = {k: int(v) for k, v in prices.items() if v > 1.0}

print(expensive)  # {'apple': 1, 'cherry': 3, 'date': 2}

##############################################################################
# 7. Dictionary comprehension - srednie ocen
##############################################################################

grades   = {'Alice': [90, 85, 92], 'Bob': [70, 75, 80], 'Charlie': [95, 88]}
averages = {name: round(sum(g) / len(g), 1) for name, g in grades.items()}

print(averages)  # {'Alice': 89.0, 'Bob': 75.0, 'Charlie': 91.5}

##############################################################################
# 8. Dictionary comprehension - odwrócenie słownika
##############################################################################

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
inverted = {v: k for k, v in original.items()}

print(inverted)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

##############################################################################
# 9. Set comprehension - unikalne pierwsze litery
##############################################################################

words       = ['cat', 'car', 'dog', 'deer', 'duck', 'cat']
first_chars = {word[0] for word in words}

print(first_chars)   # {'c', 'd'}

##############################################################################
# 10. Suma kwadratow przez generator
##############################################################################

total = sum(x**2 for x in range(1, 1001))

print(total)   # 333833500

##############################################################################
# 11. Funkcja generatora countdown
##############################################################################

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for val in countdown(5):
    print(val, end=' ')   # 5 4 3 2 1 0
print()

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2

##############################################################################
# 12. next() z wartością domyślną
##############################################################################

gen    = (x for x in range(1, 4))
first  = next(gen)
second = next(gen)
third  = next(gen)
default = next(gen, 0)

print(first, second, third)  # 1 2 3
print(default)               # 0

##############################################################################
# 13. Proste lambdy
##############################################################################

square  = lambda x: x ** 2
is_even = lambda x: x % 2 == 0

print(square(5))     # 25
print(is_even(4))    # True
print(is_even(7))    # False

##############################################################################
# 14. Sortowanie napisow na trzy sposoby
##############################################################################

words = ['banana', 'apple', 'cherry', 'date']

alphabetical = sorted(words)
by_length    = sorted(words, key=lambda w: len(w))
by_last_char = sorted(words, key=lambda w: w[-1])

print(alphabetical)   # ['apple', 'banana', 'cherry', 'date']
print(by_length)      # ['date', 'apple', 'banana', 'cherry']
print(by_last_char)   # ['banana', 'apple', 'date', 'cherry']

##############################################################################
# 15. Sortowanie dostepnych produktow wg ceny
##############################################################################

products = [
    {"name": "laptop",   "price": 2500, "stock": 5},
    {"name": "mouse",    "price": 50,   "stock": 0},
    {"name": "monitor",  "price": 800,  "stock": 3},
    {"name": "keyboard", "price": 150,  "stock": 8},
]

available_sorted = sorted(
    filter(lambda p: p["stock"] > 0, products),
    key=lambda p: p["price"]
)

for p in available_sorted:
    print(p["name"], p["price"])
# keyboard 150
# monitor 800
# laptop 2500

##############################################################################
# 16. Lambda wieloargumentowa i warunkowa
##############################################################################

max_of_two = lambda x, y: x if x > y else y
parity     = lambda x: "parzysta" if x % 2 == 0 else "nieparzysta"

print(max_of_two(3, 7))   # 7
print(max_of_two(10, 5))  # 10
print(parity(4))           # parzysta
print(parity(7))           # nieparzysta

##############################################################################
# 17. Celsius -> Fahrenheit
##############################################################################

celsius     = [0, 20, 37, 00]
fahrenheit  = list(map(lambda c: c * 9 / 5 + 32, celsius))

print(fahrenheit)   # [32.0, 68.0, 98.6, 212.0]

##############################################################################
# 18. Filtrowanie i podnoszenie do kwadratu
##############################################################################

numbers   = [-3, -1, 0, 4, 7, -2, 9]
positives = list(filter(lambda x: x > 0, numbers))
squared   = list(map(lambda x: x ** 2, positives))

print(positives)  # [4, 7, 9]
print(squared)    # [16, 49, 81]

##############################################################################
# 19. filter() + map() na napisach
##############################################################################

words      = ['hello', 'WORLD', 'Python', '123', 'foo', 'BAR']
only_alpha = filter(str.isalpha, words)
titled     = list(map(str.title, only_alpha))

print(titled)   # ['Hello', 'World', 'Python', 'Foo', 'Bar']

##############################################################################
# 20. map() na dwóch listach jednocześnie
##############################################################################

prices       = [100, 200, 350, 80]
discounts    = [10, 5, 20, 0]
final_prices = list(map(lambda x, y: x * (1 - y / 100), prices, discounts))

print(final_prices)  # [90.0, 190.0, 280.0, 80.0]
