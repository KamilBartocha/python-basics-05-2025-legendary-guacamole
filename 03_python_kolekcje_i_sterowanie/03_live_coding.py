x = [0, 1 ,"ala"]
print(x)


# list_a = [9, 8, 1, 2, 5, 7]

# list_a_sort = sorted(list_a)
# print(list_a)
# print(list_a_sort)



list_a = [9, 8, 1, 2, 5, 7]
list_a.sort()
print(list_a)


list_a.append(0)
print(list_a)

list1 = [1, 1, 1]
list2 = [2, 2, 2]
list3 = [3, 3, 3]

list_d = [list1, list2, list3]
print(list_d)

"""
 [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
 ]
"""
print("\n\n\n\n\n\n")


pesel = 2131231231

if len(str(pesel)) != 11:
    print("pesel nie poprawny")
    print(f"{len(str(pesel))} != 11")
else:
    print("pesel poprawny!")
print("Poza IF-ELSE")


# operacja1 = input("Podaj operację: Wpłać lub Wypłać: ")

# if operacja1 == "Wpłać":
#     operacja2 = input("PLN or EUR: ")
#     if operacja2 == "PLN":
#         print("Wprowadz banknoty: ")
#     elif operacja2 == "EUR":
#         print("Tylko PLN jest dozwolone")
#     else:
#         print("Niedozwolona opcja.")
# elif operacja1 == "Wypłać":
#     operacja3 = input("Karta or BLIK: ")
#     if operacja3 == "Karta":
#         print("Wprowadz kartę:")
#     elif operacja3 == "BLIK":
#         print("Podaj Blik:")
#     else:
#         print("Niedozwolona opcja.")
# else:
#     print("Niedozwolona opcja, tylko Wpłać lub Wypłać.")




pesel = 21312312310

is_pesel_valid = True if len(str(pesel)) == 11 else False
print(is_pesel_valid)



names = ["Ala", "Bonifacy", 2, "Ola"]
result = []
for name in names:
    if isinstance(name, int):
        continue
    result.append(name)

print(result)