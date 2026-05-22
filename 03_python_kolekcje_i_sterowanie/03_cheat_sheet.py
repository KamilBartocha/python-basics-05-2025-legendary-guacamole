numbers = [10, 20, 30, 40, 50]
print(numbers[1:4], numbers[::-1], numbers[::2])

fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
fruits.append('date')
fruits.insert(1, 'avocado')
fruits.remove('cherry')
popped = fruits.pop(0)
print(fruits, popped)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print(len(nums), nums.count(1), nums.index(5))
print(sorted(nums), nums)
nums.sort()
print(nums)

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4], my_tuple[::-1])

scores = {'Alice': 92, 'Bob': 78}
scores['Diana'] = 95
scores['Bob'] = 80
del scores['Bob']
print(scores, 'Alice' in scores)

phone_book = {'Alice': 500123, 'Bob': 343455}
print(list(phone_book.keys()), list(phone_book.values()))
for name, number in phone_book.items():
    print(f'{name}: {number}')

my_set = {1, 2, 3, 3, 4}
print(my_set, set([1, 2, 2, 3]))
set_a, set_b = {1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}
print(set_a | set_b, set_a & set_b, set_a - set_b, set_a ^ set_b)

score = 73
if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'F'
print(grade)

result = 'passed' if score >= 60 else 'failed'
print(result)

for char in 'Python':
    print(char, end=' ')
print()

for i in range(0, 11, 2):
    print(i, end=' ')
print()

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

count = 5
while count > 0:
    print(count, end=' ')
    count -= 1
print('Go!')

for n in range(10):
    if n == 5:
        break
    print(n, end=' ')
print()

for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=' ')
print()
