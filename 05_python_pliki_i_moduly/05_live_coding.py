f = open('05_python_pliki_i_moduly/05_file_text.txt', 'r', encoding='UTF-8')
print(f)
content = f.read()
print(content)
f.close()


f = open('05_python_pliki_i_moduly/05_file_text.txt', 'r', encoding='UTF-8')
print(f)
content = f.readline()
content2 = f.readline()

print(content)
print(content2)

f.close()

f = open('05_python_pliki_i_moduly/05_file_text.txt', 'r', encoding='UTF-8')
print(f)
content = f.readlines()

print(content)

f.close()


""" str -> read()
"Co to jest język Python?
Python jest szeroko stosowanym dynamicznym językiem programowania wysokiego poziomu, ogólnego przeznaczenia. Jego filozofia projektowania kładzie nacisk na czytelność kodu, a jego składnia pozwala programistom na wyrażanie koncepcji w mniejszej liczbie wierszy kodu niż jest to możliwe w językach takich jak C++ lub Java.
Python obsługuje wiele paradygmatów programowania, w tym programowanie obiektowe, imperatywne i funkcjonalne oraz style proceduralne. Posiada dynamiczny system typów i automatyczne zarządzanie pamięcią oraz dużą i wszechstronną bibliotekę standardową.
Najlepszym sposobem nauki języka Python są ćwiczenia i pytania z ćwiczeniami."

"""

"""list -> readlines()

[
'Co to jest język Python?\n',
'Python jest szeroko stosowanym dynamicznym językiem programowania wysokiego poziomu, ogólnego przeznaczenia. Jego filozofia projektowania kładzie nacisk na czytelność kodu, a jego składnia pozwala programistom na wyrażanie koncepcji w mniejszej liczbie wierszy kodu niż jest to możliwe w językach takich jak C++ lub Java.\n',
'Python obsługuje wiele paradygmatów programowania, w tym programowanie obiektowe, imperatywne i funkcjonalne oraz style proceduralne. Posiada dynamiczny system typów i automatyczne zarządzanie pamięcią oraz dużą i wszechstronną bibliotekę standardową.\n', 'Najlepszym sposobem nauki języka Python są ćwiczenia i pytania z ćwiczeniami.\n'
]


"""




file = open('05_python_pliki_i_moduly/05_file_text_1.txt', 'w')

for _ in range(10):
    file.write("Dowolny text\n")

file.close()



file = open('05_python_pliki_i_moduly/05_file_text_2.txt', 'a')

for _ in range(10):
    file.write("Dowolny text\n")

file.close()






file = open('05_python_pliki_i_moduly/05_file_text_3.txt', 'w')

for _ in range(10):
    file.write("Dowolny text\n")

file.close()


with open('05_python_pliki_i_moduly/05_file_text_3.txt', 'w') as file:
    file.write("blok with")

