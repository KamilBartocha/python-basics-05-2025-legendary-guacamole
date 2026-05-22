class Cat:
    def __init__(self, name, age, breed):
        self.name  = name
        self.age   = age
        self.breed = breed

    def speak(self):
        print(f"{self.name}: Meow!")

    def __str__(self):
        return f"{self.name} ({self.breed}, {self.age} lat)"

    def __repr__(self):
        return f"Cat({self.name!r}, {self.breed!r}, {self.age})"

    def __len__(self):
        return self.age


my_cat = Cat("Gatsby", 2, "Devon Rex")
my_cat.speak()
print(my_cat)
print(repr(my_cat))
print(len(my_cat))

print(type(42), type("hi"), type([]), type({}))
print(isinstance(True, int), isinstance(True, bool))

a = [1, 2, 3]
b = a
print(a is b)

c = a[:]
print(a is c, a == c)

x = 4 + 3j
print(x.real, x.imag)
print("hello world".upper(), "a,b,c".split(','))

numbers = [6, 9, 3, 1]
print(sorted(numbers), numbers)
numbers.sort()
print(numbers)


class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        print(f"{self.name}: {self.sound}!")

    def describe(self):
        print(f"I am {self.name}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        print(f"{self.name} fetches the ball!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def speak(self):
        print(f"{self.name}: Purrrr... Meow!")


rex      = Dog("Rex")
whiskers = Cat("Whiskers")

rex.speak()
rex.fetch()
rex.describe()
whiskers.speak()

print(isinstance(rex, Dog), isinstance(rex, Animal), isinstance(rex, Cat))


class Thermometer:
    def __init__(self, celsius):
        self.__celsius = celsius

    def temperature(self):
        return f"{self.__celsius}°C"


print(Thermometer(22).temperature())
