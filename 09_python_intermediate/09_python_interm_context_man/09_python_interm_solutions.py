# Solutions: 09_python_interm_context_man.ipynb
import os
import sqlite3
from contextlib import contextmanager

##############################################################################
# 1. write lines to file, read back
##############################################################################

lines = ['apple', 'banana', 'cherry', 'date']

with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')

with open('output.txt') as f:
    content = f.readlines()

print(len(content))   # 4

##############################################################################
# 2. copy_file
##############################################################################

def copy_file(src, dst):
    with open(src) as s, open(dst, 'w') as d:
        d.write(s.read())


copy_file('output.txt', 'output_copy.txt')

with open('output_copy.txt') as f:
    print(f.read())

##############################################################################
# 3. word_count
##############################################################################

def word_count(path):
    counts = {}
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    counts[word] = counts.get(word, 0) + 1
    except FileNotFoundError:
        return {}
    return counts


with open('greetings.txt', 'w') as f:
    f.write('Hello Alice\nHello Bob\n')

print(word_count('greetings.txt'))   # {'Hello': 2, 'Alice': 1, 'Bob': 1}
print(word_count('missing.txt'))     # {}

##############################################################################
# 4. Indenter
##############################################################################

class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *args):
        self.level -= 1

    def print(self, text):
        print('  ' * self.level + text)


ind = Indenter()
with ind:
    ind.print('level 1')
    with ind:
        ind.print('level 2')
    ind.print('level 1 again')
# Expected:
#   level 1
#     level 2
#   level 1 again

##############################################################################
# 5. SuppressError
##############################################################################

class SuppressError:
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exc_types):
            return True
        return False


with SuppressError(ValueError, KeyError):
    raise ValueError("ignored")   # suppressed

print("After suppress block")

try:
    with SuppressError(ValueError):
        raise TypeError("not suppressed")
except TypeError as e:
    print(f"Got: {e}")

##############################################################################
# 6. TemporaryFile
##############################################################################

class TemporaryFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, *args):
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)


with TemporaryFile('tmp_test.txt') as f:
    f.write('temporary content')

print(os.path.exists('tmp_test.txt'))   # False

##############################################################################
# 7. log_block
##############################################################################

@contextmanager
def log_block(name):
    print(f"[{name}] start")
    yield
    print(f"[{name}] end")


with log_block("data loading"):
    data = list(range(10))
# [data loading] start
# [data loading] end

##############################################################################
# 8. catch_errors - catching exception from inside the with block
##############################################################################

@contextmanager
def catch_errors(label):
    errors = []
    try:
        yield errors
    except Exception as e:
        errors.append(e)   # suppress: do not re-raise
    finally:
        print(f"[{label}] errors collected: {len(errors)}")


with catch_errors("step1") as errs:
    raise ValueError("something broke")   # suppressed

print(errs)   # [ValueError('something broke')]

with catch_errors("step2") as errs:
    x = 1 + 1   # no exception

print(errs)   # []

##############################################################################
# 9. open_write
##############################################################################

@contextmanager
def open_write(path):
    f = None
    try:
        f = open(path, 'w', encoding='utf-8')
        yield f
    except OSError as e:
        print(f"Cannot open {path}: {e}")
    finally:
        if f:
            f.close()


with open_write('test_write.txt') as f:
    f.write('hello context manager')

##############################################################################
# 10. temp_env
##############################################################################

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old


os.environ.pop('MY_VAR', None)

with temp_env('MY_VAR', 'test_value'):
    print(os.environ.get('MY_VAR'))   # test_value

print(os.environ.get('MY_VAR'))       # None

##############################################################################
# 11. ReadOnlyFile
##############################################################################

class ReadOnlyFile:
    def __init__(self, path):
        self.path = path
        self._file = None

    def __enter__(self):
        self._file = open(self.path, 'r', encoding='utf-8')
        return self

    def read(self):
        return self._file.read()

    def write(self, data):
        raise PermissionError(f"File '{self.path}' is read-only")

    def __exit__(self, *args):
        self._file.close()


with open('greetings.txt', 'w') as f:
    f.write('Hello Alice\nHello Bob\n')

with ReadOnlyFile('greetings.txt') as f:
    print(f.read())
    try:
        f.write('blocked')
    except PermissionError as e:
        print(e)

##############################################################################
# 12. managed_db
##############################################################################

@contextmanager
def managed_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


with managed_db(':memory:') as cur:
    cur.execute('CREATE TABLE notes (text TEXT)')
    cur.execute('INSERT INTO notes VALUES (?)', ('hello',))
    print(cur.execute('SELECT * FROM notes').fetchall())   # [('hello',)]

##############################################################################
# 13. APISession  (requires requests)
##############################################################################

import requests


class APISession:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = None

    def __enter__(self):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = 'MyApp/1.0'
        return self

    def get(self, endpoint):
        response = self.session.get(self.base_url + endpoint)
        response.raise_for_status()
        return response.json()

    def __exit__(self, *args):
        self.session.close()


with APISession('https://jsonplaceholder.typicode.com') as api:
    data = api.get('/users/1')
    print(data['name'])   # Leanne Graham
