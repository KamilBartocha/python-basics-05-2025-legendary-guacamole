f = open('05_file_text.txt', 'r')
print(f.name, f.mode)
f.close()

with open('05_file_text.txt', 'r') as f:
    content = f.read()
print(content[:80])

with open('05_file_text.txt', 'r') as f:
    lines = f.readlines()
print(f'Lines: {len(lines)}, last: {lines[-1].strip()}')

with open('output.txt', 'w') as f:
    f.write('Hello, Python!\n')
    f.write('Second line\n')

with open('output.txt', 'a') as f:
    f.write('Third line - appended\n')

with open('output.txt', 'r') as f:
    print(f.read())

import math
import math as m
from math import sqrt, pi

print(math.pi, m.floor(3.7), m.ceil(3.2), sqrt(25), pi)
print(__name__)
