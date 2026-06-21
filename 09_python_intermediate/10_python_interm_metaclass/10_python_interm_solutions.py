# Solutions: 10_python_interm_metaclass.ipynb
import functools

##############################################################################
# 1. metaclass inspection of built-in types
##############################################################################

for typ in [int, str, list, dict]:
    print(f"type({typ.__name__}) = {type(typ)}")

for typ in [int, str, list]:
    print(f"isinstance({typ.__name__}, type) = {isinstance(typ, type)}")

##############################################################################
# 2. Rectangle via type()
##############################################################################

def rect_init(self, width, height):
    self.width  = width
    self.height = height

def rect_area(self):
    return self.width * self.height


Rectangle = type('Rectangle', (object,), {
    'default_color': 'red',
    '__init__': rect_init,
    'area':     rect_area,
})

r = Rectangle(4, 6)
print(r.area())          # 24
print(r.default_color)   # red

##############################################################################
# 3. make_class
##############################################################################

def make_class(name, attrs):
    return type(name, (object,), attrs)


Config = make_class('Config', {'debug': True, 'port': 8080})
c = Config()
print(c.debug)               # True
print(c.port)                # 8080
print(type(c).__name__)      # Config
print(isinstance(c, object)) # True

##############################################################################
# 4. UpperAttrsMeta
##############################################################################

class UpperAttrsMeta(type):
    def __new__(cls, name, bases, dct):
        for key in dct:
            if not key.startswith('__') and not key.isupper():
                raise TypeError(
                    f"Attribute '{key}' in class '{name}' must be UPPERCASE"
                )
        return super().__new__(cls, name, bases, dct)


class Config2(metaclass=UpperAttrsMeta):
    HOST = 'localhost'
    PORT = 8080

print(Config2.HOST)   # localhost

try:
    class BadConfig(metaclass=UpperAttrsMeta):
        host = 'localhost'
except TypeError as e:
    print(e)

##############################################################################
# 5. VersionedMeta
##############################################################################

class VersionedMeta(type):
    def __new__(cls, name, bases, dct):
        if 'version' not in dct:
            dct['version'] = '1.0'
        dct['created_by'] = 'VersionedMeta'
        return super().__new__(cls, name, bases, dct)


class Alpha(metaclass=VersionedMeta):
    pass

class Beta(metaclass=VersionedMeta):
    version = '2.5'


print(Alpha.version)     # 1.0
print(Beta.version)      # 2.5
print(Alpha.created_by)  # VersionedMeta
print(Beta.created_by)   # VersionedMeta

##############################################################################
# 6. ReadOnlyMeta
##############################################################################

class ReadOnlyMeta(type):
    def __setattr__(cls, name, value):
        if hasattr(cls, name):
            raise AttributeError(
                f"Cannot modify read-only attribute '{name}'"
            )
        super().__setattr__(name, value)


class Constants(metaclass=ReadOnlyMeta):
    PI    = 3.14159
    SPEED = 299_792_458


print(Constants.PI)   # 3.14159

try:
    Constants.PI = 3
except AttributeError as e:
    print(e)

##############################################################################
# 7. ModelMeta - validation + auto-adding
##############################################################################

class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        if bases and 'fields' not in dct:
            raise TypeError(f"'{name}' must define 'fields'")
        if 'get_fields' not in dct:
            def get_fields(self):
                return type(self).fields
            dct['get_fields'] = get_fields
        return super().__new__(cls, name, bases, dct)


class Model(metaclass=ModelMeta):
    pass

class User(Model):
    fields = ['name', 'email']


u = User()
print(u.get_fields())   # ['name', 'email']

try:
    class Item(Model):
        pass
except TypeError as e:
    print(e)

##############################################################################
# 8. TypeRegistryMeta - register only subclasses
##############################################################################

class TypeRegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if bases:
            cls.registry[name] = new_class
        return new_class


class Animal(metaclass=TypeRegistryMeta):
    pass

class Dog(Animal): pass
class Cat(Animal): pass


print(TypeRegistryMeta.registry)   # {'Dog': ..., 'Cat': ...}

##############################################################################
# 9. CountInstancesMeta
##############################################################################

class CountInstancesMeta(type):
    def __new__(cls, name, bases, dct):
        dct['instance_count'] = 0
        original_init = dct.get('__init__')

        def __init__(self, *args, **kwargs):
            type(self).instance_count += 1
            if original_init:
                original_init(self, *args, **kwargs)

        dct['__init__'] = __init__
        return super().__new__(cls, name, bases, dct)


class Car(metaclass=CountInstancesMeta):
    pass


Car()
Car()
Car()
print(Car.instance_count)   # 3

##############################################################################
# 10. AbstractMeta
##############################################################################

class AbstractMeta(type):
    def __call__(cls, *args, **kwargs):
        if cls.__dict__.get('abstract', False):
            raise TypeError(
                f"Cannot instantiate abstract class '{cls.__name__}'"
            )
        return super().__call__(*args, **kwargs)


class Shape(metaclass=AbstractMeta):
    abstract = True

class Circle(Shape):
    def __init__(self, r):
        self.r = r


c = Circle(5)
print(c.r)    # 5

try:
    Shape()
except TypeError as e:
    print(e)

##############################################################################
# 11. Command registry via __init_subclass__
##############################################################################

class Command:
    commands = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Command.commands[cls.__name__.lower()] = cls


class HelpCommand(Command):
    pass

class QuitCommand(Command):
    pass


print(Command.commands)
# {'helpcommand': <class 'HelpCommand'>, 'quitcommand': <class 'QuitCommand'>}

##############################################################################
# 12. Validator with __init_subclass__
##############################################################################

class Validator:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if 'validate' not in cls.__dict__:
            raise TypeError(
                f"'{cls.__name__}' must implement validate()"
            )


class EmailValidator(Validator):
    def validate(self, value):
        return '@' in value


print(EmailValidator().validate('alice@example.com'))   # True

try:
    class BadValidator(Validator):
        pass
except TypeError as e:
    print(e)

##############################################################################
# 13. Comparison: metaclass vs __init_subclass__
##############################################################################

class PluginMeta(type):
    registry = {}
    def __new__(cls, name, bases, dct):
        if bases and 'run' not in dct:
            raise TypeError(f"'{name}' must implement run()")
        new_cls = super().__new__(cls, name, bases, dct)
        if bases:
            cls.registry[name] = new_cls
        return new_cls

class BasePlugin(metaclass=PluginMeta): pass
class EmailPlugin(BasePlugin):
    def run(self): return 'email'


class Plugin2:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if 'run' not in cls.__dict__:
            raise TypeError(f"'{cls.__name__}' must implement run()")
        Plugin2.registry[cls.__name__] = cls

class LogPlugin2(Plugin2):
    def run(self): return 'log'


print(PluginMeta.registry)   # {'EmailPlugin': ...}
print(Plugin2.registry)      # {'LogPlugin2': ...}

##############################################################################
# 14. Vehicle with keyword args in __init_subclass__
##############################################################################

class Vehicle:
    def __init_subclass__(cls, fuel_type='unknown', seats=5, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.fuel_type = fuel_type
        cls.seats     = seats


class Car(Vehicle, fuel_type='petrol', seats=5):
    pass

class ElectricBike(Vehicle, fuel_type='electric', seats=2):
    pass

class Bicycle(Vehicle):
    pass


print(Car.fuel_type)           # petrol
print(ElectricBike.fuel_type)  # electric
print(Bicycle.fuel_type)       # unknown
print(ElectricBike.seats)      # 2
