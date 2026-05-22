from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result_imperative = []
for n in numbers:
    if n % 2 == 0:
        result_imperative.append(n ** 2)

result_functional = [n ** 2 for n in numbers if n % 2 == 0]
print(result_imperative, result_functional)

hypotenuse = lambda a, b: ((a * a) + (b * b)) ** 0.5
print(hypotenuse(3, 5))

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sorted(people))
print(sorted(people, key=lambda p: p[1]))
print(sorted(people, key=lambda p: p[1], reverse=True))

print([x ** 3 for x in range(5)])
print([n ** 2 for n in range(1, 11) if n % 2 != 0])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for row in matrix for num in row])

print({char for char in "abracadabra"})
print({len(w) for w in ["python", "java", "go", "rust"]})

names, scores = ["Alice", "Bob", "Charlie"], [95, 87, 92]
results = {name: score for name, score in zip(names, scores)}
print(results)

text = "google.com"
print({char: text.count(char) for char in text})

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda n: n ** 2, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))
print(list(map(str.upper, ["hello", "world"])))
print(list(map(abs, [-3, -1, 0, 2, 5])))

print(reduce(lambda acc, n: acc + n, numbers))
print(reduce(lambda acc, n: acc * n, numbers))
print(reduce(lambda a, b: a if a > b else b, numbers))

words = ["functional", "programming", "in", "Python"]
print(reduce(lambda acc, w: acc + " " + w, words, "Topics:"))

squares_gen = (x ** 2 for x in range(10))
for val in squares_gen:
    print(val, end=" ")
print()

print(sum(x ** 2 for x in range(1, 101)))
print(max(x for x in range(1, 101) if x % 2 == 0))
print(any(x > 90 for x in [70, 85, 95, 60]))
print(all(x > 0 for x in [1, 2, 3]))
