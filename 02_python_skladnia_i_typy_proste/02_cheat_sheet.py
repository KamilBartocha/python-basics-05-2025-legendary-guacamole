name = "Alice"
age = 25

print("Imię: " + name)
# Imię: Alice
print("Imię: {}".format(name))
# Imię: Alice
print(f"Imię: {name}, wiek: {age}")
# Imię: Alice, wiek: 25

counter = 0
price = 19.99
counter += 1
price *= 1.23
print(counter, f"{price:.2f}")
# 1 24.59

print(type(42), type(3.14), type(True), type('hello'), type([1, 2]), type({'a': 1}))
# <class 'int'> <class 'float'> <class 'bool'> <class 'str'> <class 'list'> <class 'dict'>

print(3 + 2, 5 / 2, 5 // 2, 5 % 2, 2 ** 8)
# 5 2.5 2 1 256
print(3 + 5 * 0.5, (3 + 5) * 0.5)
# 5.5 4.0

x = 5
print(x == 5, x != 5, x > 3, x >= 5)
# True False True True
print(not True, True and False, True or False)
# False False True

age = 20
print(age >= 18 and True)
# True
print(0 or 'default')
# default

a, b = 5, 7
a, b = b, a
print(f'a={a}, b={b}')
# a=7, b=5

print(bool(0), bool(''), bool([]), bool(42))
# False False False True

x = None
print(x, type(x))
# None <class 'NoneType'>

scores = {'Alice': 95}
print(scores.get('Bob'), scores.get('Bob', 0))
# None 0

print(isinstance(42, int), isinstance(True, int), isinstance(True, bool))
# True True True

print(float(7), int(3.99), round(3.99))
# 7.0 3 4
print(int('42'), 'Age: ' + str(25))
# 42 Age: 25

word = "Python"
print(word[0], word[-1], word[0:2], word[::-1], len(word))
# P n Py nohtyP 6
print("J" + word[1:])
# Jython

text = 'Hello, World!'
print(text.upper(), text.lower())
# HELLO, WORLD! hello, world!
print(text.replace('o', '0'))
# Hell0, W0rld!
print(text.count('l'), text.split(', '), text.startswith('Hello'))
# 3 ['Hello', 'World!'] True
print('   python   '.strip())
# python
print("Linia 1\nLinia 2", "Kol 1\tKol 2")
# Linia 1
# Linia 2 Kol 1	Kol 2
print(r"C:\Users\name")
# C:\Users\name
print("-" * 30)
