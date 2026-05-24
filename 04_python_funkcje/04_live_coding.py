def fibonacci_numbers(n):
    """Returns Fibonacci numbers less than n.
    Ale super funkcja
    """
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def print_10_20():
    for number in range(10, 21):
        print(number)

print_10_20()

def seperate_examples():
    print('\n\n\n')
    print('-' * 100)
    print('\n')

seperate_examples()

def add_three(x1, x2, x3):
    result = x1 + x2 + x3
    return result

result = add_three(1, 2, 5)
print(result)



seperate_examples()

def add_three2(x1=0, x2=0, x3=0):
    result = x1 + x2 + x3
    return result

result = add_three2(1, 2)
print(result)

seperate_examples()




def greet(name, age):
    """_summary_

    Args:
        name (_type_): _description_
        age (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(f"Cześć, jesteś {name} i masz {age} lat")
    x = "ala"
    return x

greet("Ala", 30)


greet(age=40, name="Ola")

fibonacci_numbers(10)
# print(x)

counter = 12

def increment():
    global counter
    counter += 1


increment()
increment()
print(counter)  # 2
greet()


