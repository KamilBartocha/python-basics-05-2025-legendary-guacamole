def greet(name="World"):
    print(f"Hello, {name}!")

greet("Alice")
greet()


def add(x, y):
    """Returns the sum of x and y."""
    return x + y

print(add(2, 3))
help(add)


def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item("a"))
print(add_item("b"))


def calc_sum(a, b):
    return a + b

def print_sum(a, b):
    print(a + b)

result = calc_sum(4, 5)
print(result)
print(print_sum(4, 5))


def fibonacci_numbers(n):
    """Returns Fibonacci numbers less than n."""
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_numbers(100))


x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)

outer()
print(x)

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)


def sum_recur(n):
    if n == 0:
        return 0
    return n + sum_recur(n - 1)

print(sum_recur(3))


def total(*args):
    return sum(args)

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

def mixed(required, *args, **kwargs):
    print(required, args, kwargs)

print(total(1, 2, 3))
show_info(name="Alice", age=30)
mixed("hello", 1, 2, color="red")
