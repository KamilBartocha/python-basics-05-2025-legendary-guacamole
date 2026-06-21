# Solutions: 06_python_interm_json.ipynb
import json

##############################################################################
# 1. dict -> JSON string
##############################################################################

product = {
    "name": "keyboard",
    "price": 150,
    "available": True
}

result = json.dumps(product, indent=2)

print(type(result))   # <class 'str'>
print(result)

##############################################################################
# 2. JSON string -> dict
##############################################################################

book_json = '{"title": "1984", "author": "Orwell", "year": 1949}'

book = json.loads(book_json)

print(book["title"])   # 1984
print(book["year"])    # 1949

##############################################################################
# 3. list of dicts - round-trip
##############################################################################

orders = [
    {"id": 1, "item": "laptop", "qty": 2},
    {"id": 2, "item": "mouse",  "qty": 5},
]

json_str = json.dumps(orders)
restored = json.loads(json_str)

print(orders == restored)   # True

##############################################################################
# 4. Mapowanie typów Python -> JSON
##############################################################################

data = {
    "nothing": None,
    "flag":    True,
    "off":     False,
    "tags":    (1, 2, 3),
}

json_str = json.dumps(data)
restored = json.loads(json_str)

print(restored["nothing"] is None)   # True  (null -> None)
print(type(restored["flag"]))        # <class 'bool'>
print(type(restored["tags"]))        # <class 'list'>  (tuple -> list!)

##############################################################################
# 5. sort_keys
##############################################################################

settings = {"timeout": 30, "host": "localhost", "debug": True}

result = json.dumps(settings, sort_keys=True)

print(result)
# {"debug": true, "host": "localhost", "timeout": 30}

##############################################################################
# 6. write to file
##############################################################################

user = {"name": "Zofia", "age": 28, "city": "Kraków"}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, indent=4, ensure_ascii=False)

with open("user.json", encoding="utf-8") as f:
    print(f.read())

##############################################################################
# 7. read, modify, write back
##############################################################################

with open("user.json", encoding="utf-8") as f:
    data = json.load(f)

data["age"] = data["age"] + 1

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(data["age"])   # 29

##############################################################################
# 8. json.dumps() z kombinacją parametrów
##############################################################################

config3 = {"port": 8080, "name": "Aplikacja", "debug": True, "host": "localhost"}

# a) kompaktowy
a = json.dumps(config3)
print("Kompaktowy:", a)

# b) indent=2, sort_keys=True
b = json.dumps(config3, indent=2, sort_keys=True)
print("Posortowany:\n", b)

# c) indent=4, sort_keys=True, ensure_ascii=False
c = json.dumps(config3, indent=4, sort_keys=True, ensure_ascii=False)
print("Pełny:\n", c)

##############################################################################
# 9. write and read a list
##############################################################################

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob",   "grade": "B"},
    {"name": "Carol", "grade": "A"},
]

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

with open("students.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded[1]["name"])   # Bob

##############################################################################
# 10. read nested config
##############################################################################

config = {
    "database": {"host": "localhost", "port": 5432, "name": "appdb"},
    "server":   {"host": "0.0.0.0",  "port": 8080}
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

print(config["database"]["host"])   # localhost
print(config["server"]["port"])     # 8080

##############################################################################
# 11. filter JSON data and write result
##############################################################################

orders = [
    {"id": 1, "item": "laptop",  "status": "done"},
    {"id": 2, "item": "mouse",   "status": "pending"},
    {"id": 3, "item": "monitor", "status": "done"},
    {"id": 4, "item": "desk",    "status": "pending"},
]

done_orders = [o for o in orders if o["status"] == "done"]

with open("done_orders.json", "w", encoding="utf-8") as f:
    json.dump(done_orders, f, indent=2)

print(len(done_orders))       # 2
print(done_orders[0]["id"])   # 1

##############################################################################
# 12. ensure_ascii=False z polskimi znakami
##############################################################################

polish_names = [
    {"name": "Józef",      "city": "Łódź"},
    {"name": "Małgorzata", "city": "Gdańsk"},
]

with open("polish.json", "w", encoding="utf-8") as f:
    json.dump(polish_names, f, indent=2, ensure_ascii=False)

with open("polish.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded[0]["name"])   # Józef
print(loaded[1]["city"])   # Gdańsk

with open("polish.json", encoding="utf-8") as f:
    raw = f.read()
print("\\u" not in raw)    # True - polskie znaki zapisane bezpośrednio

##############################################################################
# 13. validate multiple JSON strings
##############################################################################

candidates = [
    '{"name": "Alice", "age": 30}',
    '{"name": "Bob", age: 25}',
    '{"name": "Carol", "age": 22}',
]

for s in candidates:
    try:
        data = json.loads(s)
        print(f"{data['name']}: {data['age']}")
    except json.JSONDecodeError as e:
        print(f"Error: {e}")

# Alice: 30
# Error: ...
# Carol: 22

##############################################################################
# 14. load_or_default
##############################################################################

def load_or_default(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


result = load_or_default("config.json", {})
print(type(result))   # <class 'dict'>

missing = load_or_default("missing.json", {"status": "empty"})
print(missing)        # {'status': 'empty'}

##############################################################################
# 15. update_json
##############################################################################

def update_json(path, key, value):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        data[key] = value
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")


update_json("config.json", "server", {"host": "0.0.0.0", "port": 9000})

with open("config.json", encoding="utf-8") as f:
    data = json.load(f)
print(data["server"]["port"])   # 9000

##############################################################################
# 16. get_field - obsługa JSONDecodeError i KeyError
##############################################################################

def get_field(data_json, key):
    try:
        data = json.loads(data_json)
        return data[key]
    except json.JSONDecodeError:
        return None
    except KeyError:
        return None


print(get_field('{"name": "Alice", "age": 30}', "name"))   # Alice
print(get_field('{"name": "Alice"}', "age"))                # None  (KeyError)
print(get_field('not valid json', "name"))                   # None  (JSONDecodeError)
