# Solutions: 01_python_interm_oop_advanced.ipynb
##############################################################################
# 1. Rectangle
##############################################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16

##############################################################################
# 2. Book
##############################################################################

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"


book = Book("1984", "George Orwell", 1949)
print(book.get_info())
# '1984' by George Orwell, published in 1949

##############################################################################
# 3. ShoppingCart
##############################################################################

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        print(f"{name} not found in cart.")

    def total(self):
        return sum(item["price"] for item in self.items)


cart = ShoppingCart()
cart.add_item("Laptop", 1999)
cart.add_item("Mouse", 25)
print(cart.total())       # 2024
cart.remove_item("Mouse")
print(cart.total())       # 1999

##############################################################################
# 4. Circle
##############################################################################

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print(f"{c.area():.2f}")          # 78.54
print(f"{c.circumference():.2f}") # 31.42

##############################################################################
# 5. BankAccount
##############################################################################

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())   # 1500
account.withdraw(200)
print(account.get_balance())   # 1300
account.withdraw(2000)         # Insufficient funds.
print(account.get_balance())   # 1300

##############################################################################
# 6. Student
##############################################################################

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def highest(self):
        return max(self.grades)

    def lowest(self):
        return min(self.grades)


s = Student("Bob")
s.add_grade(85)
s.add_grade(92)
s.add_grade(78)
print(s.average())   # 85.0
print(s.highest())   # 92
print(s.lowest())    # 78

##############################################################################
# 7. Animal + Dog
##############################################################################

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"Animal(name: '{self.name}')"


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def __str__(self):
        return f"Dog(name: '{self.name}')"


dog = Dog("Rex")
print(dog)               # Dog(name: 'Rex')
print(dog.make_sound())  # Woof! Woof!

##############################################################################
# 8. Shape + Circle + Rectangle
##############################################################################

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(3)
rect = Rectangle(4, 5)
print(f"Circle area: {circle.area():.2f}")    # 28.27
print(f"Rectangle area: {rect.area()}")       # 20

##############################################################################
# 9. Employee + Manager
##############################################################################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name: '{self.name}', salary: {self.salary})"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.team = []

    def add_to_team(self, employee):
        self.team.append(employee)

    def __str__(self):
        members = len(self.team)
        return (
            f"Manager(name: '{self.name}', salary: {self.salary}, "
            f"department: '{self.department}', team size: {members})"
        )


emp = Employee("Bob", 5000)
mgr = Manager("Alice", 8000, "Engineering")
mgr.add_to_team(emp)
print(emp)
print(mgr)
print(Manager.__mro__)

##############################################################################
# 10. Vehicle + ElectricCar
##############################################################################

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}), battery: {self.battery_capacity} kWh"


car = Vehicle("Toyota", "Corolla", 2020)
ev = ElectricCar("Tesla", "Model 3", 2023, 75)
print(car)   # Toyota Corolla (2020)
print(ev)    # Tesla Model 3 (2023), battery: 75 kWh

##############################################################################
# 11. Animal -> Bird -> Parrot
##############################################################################

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def speak(self):
        return "Tweet!"


class Parrot(Bird):
    def __init__(self, name, wingspan, vocabulary):
        super().__init__(name, wingspan)
        self.vocabulary = vocabulary

    def speak(self):
        return self.vocabulary[0]


parrot = Parrot("Polly", 30, ["Hello!", "Pretty bird!", "Squawk!"])
print(parrot.name)       # Polly
print(parrot.wingspan)   # 30
print(parrot.speak())    # Hello!
print(Parrot.__mro__)

##############################################################################
# 12. Thermometer
##############################################################################

class Thermometer:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_temp(self):
        return self.__celsius

    def set_temp(self, value):
        if value < -273.15:
            print("Invalid temperature.")
        else:
            self.__celsius = value


t = Thermometer(20)
print(t.get_temp())   # 20
t.set_temp(37)
print(t.get_temp())   # 37
t.set_temp(-300)      # Invalid temperature.
print(t.get_temp())   # 37

##############################################################################
# 13. SecureCounter
##############################################################################

class SecureCounter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count > 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def get_count(self):
        return self.__count


counter = SecureCounter()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_count())   # 3
counter.decrement()
print(counter.get_count())   # 2
counter.reset()
print(counter.get_count())   # 0
counter.decrement()
print(counter.get_count())   # 0 (not negative)

##############################################################################
# 14. Person z walidacją
##############################################################################

class Person:
    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if not value:
            print("Invalid name.")
        else:
            self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not (0 <= value <= 150):
            print("Invalid age.")
        else:
            self.__age = value


p = Person("Alice", 30)
print(p.get_name())   # Alice
print(p.get_age())    # 30
p.set_age(200)        # Invalid age.
p.set_name("")        # Invalid name.
print(p.get_age())    # 30

##############################################################################
# 15. Inventory (protected attribute)
##############################################################################

class Inventory:
    def __init__(self):
        self._items = []
        self._capacity = 10

    def add_item(self, item):
        if len(self._items) < self._capacity:
            self._items.append(item)
        else:
            print("Inventory full.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)

    def get_items(self):
        return self._items


inv = Inventory()
inv.add_item("sword")
inv.add_item("shield")
print(inv.get_items())   # ['sword', 'shield']
inv.remove_item("sword")
print(inv.get_items())   # ['shield']
# Dostep do chronionego atrybutu (mozliwy, ale niezalecany):
print(inv._items)        # ['shield']

##############################################################################
# 16. Safe (name mangling)
##############################################################################

class Safe:
    def __init__(self, code):
        self.__code = code

    def check_code(self, code):
        return self.__code == code

    def change_code(self, old_code, new_code):
        if self.check_code(old_code):
            self.__code = new_code
        else:
            print("Wrong code.")


safe = Safe("1234")
print(safe.check_code("0000"))   # False
print(safe.check_code("1234"))   # True
safe.change_code("1234", "5678")
print(safe.check_code("5678"))   # True
# Name mangling - dostep przez _ClassName__attr:
print(safe._Safe__code)           # 5678

##############################################################################
# 17. CreditCard
##############################################################################

class CreditCard:
    def __init__(self, number, limit):
        self.__number = number
        self.__balance = 0
        self.__limit = limit

    def charge(self, amount):
        if self.__balance + amount > self.__limit:
            print("Limit exceeded.")
        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def get_masked_number(self):
        return f"****{self.__number[-4:]}"


card = CreditCard("1234567890001234", 5000)
print(card.get_masked_number())   # ****1234
card.charge(1000)
print(card.get_balance())         # 1000
card.charge(5000)                 # Limit exceeded.
print(card.get_balance())         # 1000

##############################################################################
# 18. Point
##############################################################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1)           # Point(1, 2)
print(repr(p1))     # Point(x=1, y=2)
print(p1 == p2)     # True
print(p1 == p3)     # False

##############################################################################
# 19. Fraction
##############################################################################

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1 + f2
print(f1)   # 1/2
print(f2)   # 1/4
print(f3)   # 6/8

##############################################################################
# 20. Bag
##############################################################################

class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_bag = Bag()
        new_bag.items = self.items + other.items
        return new_bag

    def __str__(self):
        return "Bag: " + ", ".join(self.items)


bag1 = Bag()
bag1.add("apple")
bag1.add("banana")
bag2 = Bag()
bag2.add("cherry")
print(len(bag1))     # 2
bag3 = bag1 + bag2
print(len(bag3))     # 3
print(bag3)          # Bag: apple, banana, cherry

##############################################################################
# 21. Temperature
##############################################################################

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        return f"Temperature({self.celsius})"

    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        return False


t1 = Temperature(25)
t2 = Temperature(25)
t3 = Temperature(100)
print(t1)           # 25°C
print(repr(t1))     # Temperature(25)
print(t1 == t2)     # True
print(t1 == t3)     # False

##############################################################################
# 22. Vector
##############################################################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)                     # Vector(1, 2)
print(v1 + v2)                # Vector(4, 6)
print(v1 * 3)                 # Vector(3, 6)
print(v1 == Vector(1, 2))     # True

##############################################################################
# 23. Stack
##############################################################################

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self._items:
            return self._items.pop()
        return None

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Stack{self._items}"

    def __eq__(self, other):
        if isinstance(other, Stack):
            return self._items == other._items
        return False


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s2 = Stack()
s2.push(1)
s2.push(2)
s2.push(3)
print(len(s1))      # 3
print(s1)           # Stack[1, 2, 3]
print(s1 == s2)     # True
print(s1.pop())     # 3
print(len(s1))      # 2

##############################################################################
# 24. Counter z metodą klasową
##############################################################################

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def reset_count(cls):
        cls.count = 0


c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())   # 3
Counter.reset_count()
print(Counter.get_count())   # 0

##############################################################################
# 25. Rectangle z factory method
##############################################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)


rect = Rectangle(4, 6)
square = Rectangle.from_square(5)
print(rect.area())                  # 24
print(square.area())                # 25
print(square.width, square.height)  # 5 5

##############################################################################
# 26. Pizza z factory methods
##############################################################################

class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls("M", ["tomato", "mozzarella"])

    @classmethod
    def pepperoni(cls):
        return cls("L", ["tomato", "mozzarella", "pepperoni"])

    def __str__(self):
        return f"Pizza {self.size}: {', '.join(self.toppings)}"


p1 = Pizza.margherita()
p2 = Pizza.pepperoni()
print(p1)   # Pizza M: tomato, mozzarella
print(p2)   # Pizza L: tomato, mozzarella, pepperoni

##############################################################################
# 27. TemperatureConverter
##############################################################################

class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def describe(self):
        return f"{self.celsius}°C"

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9


t = TemperatureConverter(100)
print(t.describe())                                    # 100°C
print(TemperatureConverter.celsius_to_fahrenheit(100)) # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))  # 0.0

##############################################################################
# 28. User
##############################################################################

class User:
    _user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User._user_count += 1

    def __str__(self):
        return f"User: {self.username} ({self.email})"

    @classmethod
    def get_user_count(cls):
        return cls._user_count

    @classmethod
    def create_guest(cls):
        return cls("guest", "guest@example.com")

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


u1 = User("alice", "alice@example.com")
u2 = User.create_guest()
print(User.get_user_count())                  # 2
print(u1)                                     # User: alice (alice@example.com)
print(u2)                                     # User: guest (guest@example.com)
print(User.is_valid_email("test@test.com"))   # True
print(User.is_valid_email("invalid"))         # False
