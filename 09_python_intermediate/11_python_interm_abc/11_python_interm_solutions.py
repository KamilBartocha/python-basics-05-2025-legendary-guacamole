"""11 Python intermediate - Abstrakcyjne klasy bazowe (abc) - rozwiązania."""
from abc import ABC, abstractmethod
import json
import math


# ---------------------------------------------------------------------------
# Ćw. 1: Animal - Dog, Bird
# ---------------------------------------------------------------------------
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str: ...

    @abstractmethod
    def move(self) -> str: ...


class Dog(Animal):
    def speak(self) -> str: return "Woof!"
    def move(self) -> str: return "runs"


class Bird(Animal):
    def speak(self) -> str: return "Tweet!"
    def move(self) -> str: return "flies"


dog = Dog()
bird = Bird()
print(dog.speak(), dog.move())
print(bird.speak(), bird.move())


# ---------------------------------------------------------------------------
# Ćw. 2: Vehicle - Car, Bicycle
# ---------------------------------------------------------------------------
class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str: ...

    @abstractmethod
    def stop(self) -> str: ...

    @property
    @abstractmethod
    def max_speed(self) -> int: ...


class Car(Vehicle):
    def start(self) -> str: return "Engine started"
    def stop(self) -> str: return "Engine stopped"

    @property
    def max_speed(self) -> int: return 200


class Bicycle(Vehicle):
    def start(self) -> str: return "Pedaling"
    def stop(self) -> str: return "Braking"

    @property
    def max_speed(self) -> int: return 30


car = Car()
bike = Bicycle()
print(car.max_speed, car.start())
print(bike.max_speed, bike.start())


# ---------------------------------------------------------------------------
# Ćw. 3: Serializable - Person
# ---------------------------------------------------------------------------
class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict): ...


class Person(Serializable):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_dict(self) -> dict:
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["age"])


p = Person("Alice", 30)
data = p.to_dict()
print(data)
p2 = Person.from_dict(data)
print(p2.name, p2.age)


# ---------------------------------------------------------------------------
# Ćw. 4: Logger - ConsoleLogger, FileLogger
# ---------------------------------------------------------------------------
class Logger(ABC):
    @property
    @abstractmethod
    def level(self) -> str: ...

    @abstractmethod
    def log(self, message: str) -> None: ...


class ConsoleLogger(Logger):
    @property
    def level(self) -> str: return "INFO"

    def log(self, message: str) -> None:
        print(f"[{self.level}] {message}")


class FileLogger(Logger):
    def __init__(self, filepath: str):
        self.filepath = filepath

    @property
    def level(self) -> str: return "DEBUG"

    def log(self, message: str) -> None:
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"[{self.level}] {message}\n")


logger = ConsoleLogger()
print(logger.level)
logger.log("Hello!")


# ---------------------------------------------------------------------------
# Ćw. 5: Parser - JsonParser
# ---------------------------------------------------------------------------
class Parser(ABC):
    @abstractmethod
    def parse(self, text: str) -> dict: ...

    @abstractmethod
    def format(self, data: dict) -> str: ...

    @classmethod
    @abstractmethod
    def supported_format(cls) -> str: ...


class JsonParser(Parser):
    def parse(self, text: str) -> dict:
        return json.loads(text)

    def format(self, data: dict) -> str:
        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def supported_format(cls) -> str:
        return "json"


p = JsonParser()
data = p.parse('{"key": "value"}')
print(JsonParser.supported_format(), data)
print(p.format({"x": 1}))


# ---------------------------------------------------------------------------
# Ćw. 6: Validator - RangeValidator, LengthValidator
# ---------------------------------------------------------------------------
class Validator(ABC):
    @abstractmethod
    def validate(self, value) -> bool: ...

    @abstractmethod
    def error_message(self) -> str: ...

    def check(self, value) -> None:
        if not self.validate(value):
            raise ValueError(self.error_message())


class RangeValidator(Validator):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def validate(self, value) -> bool:
        return self.min_val <= value <= self.max_val

    def error_message(self) -> str:
        return f"Value must be between {self.min_val} and {self.max_val}"


class LengthValidator(Validator):
    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def validate(self, value) -> bool:
        return self.min_len <= len(value) <= self.max_len

    def error_message(self) -> str:
        return f"Length must be between {self.min_len} and {self.max_len}"


rv = RangeValidator(0, 00)
rv.check(50)
print("RangeValidator(50): OK")
lv = LengthValidator(3, 10)
try:
    lv.check("hi")
except ValueError as e:
    print(f"LengthValidator('hi'): {e}")


# ---------------------------------------------------------------------------
# Ćw. 7: Converter - CelsiusToFahrenheit, KilometersToMiles
# ---------------------------------------------------------------------------
class Converter(ABC):
    @staticmethod
    @abstractmethod
    def unit() -> str: ...

    @abstractmethod
    def convert(self, value: float) -> float: ...


class CelsiusToFahrenheit(Converter):
    @staticmethod
    def unit() -> str: return "°F"

    def convert(self, value: float) -> float:
        return value * 9 / 5 + 32


class KilometersToMiles(Converter):
    @staticmethod
    def unit() -> str: return "mi"

    def convert(self, value: float) -> float:
        return value * 0.621371


print(CelsiusToFahrenheit.unit())
print(CelsiusToFahrenheit().convert(100))
print(KilometersToMiles.unit())
print(KilometersToMiles().convert(10))


# ---------------------------------------------------------------------------
# Ćw. 8: Iterable_ z __subclasshook__
# ---------------------------------------------------------------------------
class Iterable_(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Iterable_:
            return hasattr(subclass, "__iter__")
        return NotImplemented


for t in [list, str, dict, int]:
    print(f"{t.__name__}: {issubclass(t, Iterable_)}")


# ---------------------------------------------------------------------------
# Ćw. 9: Printable z register
# ---------------------------------------------------------------------------
class Printable(ABC):
    @abstractmethod
    def pretty_print(self) -> None: ...


class OldReport:
    def pretty_print(self):
        print("OldReport")


print(isinstance(OldReport(), Printable))   # False
Printable.register(OldReport)
print(isinstance(OldReport(), Printable))   # True


# ---------------------------------------------------------------------------
# Ćw. 10: Plugin z REGISTRY przez __init_subclass__
# ---------------------------------------------------------------------------
class Plugin(ABC):
    REGISTRY: dict = {}

    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def execute(self) -> None: ...

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "__abstractmethods__", None):
            Plugin.REGISTRY[cls.__name__] = cls


class HelloPlugin(Plugin):
    def name(self) -> str: return "hello"
    def execute(self) -> None: print("Hello, plugin!")


class GoodbyePlugin(Plugin):
    def name(self) -> str: return "goodbye"
    def execute(self) -> None: print("Goodbye!")


print(Plugin.REGISTRY)
for plugin_cls in Plugin.REGISTRY.values():
    plugin_cls().execute()
