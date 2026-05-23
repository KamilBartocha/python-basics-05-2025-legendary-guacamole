name = "Ala"
age = 30

print(name)
print(f"name: {name}, age: {age}")
##################################



print("ala") # print(x)
# print(x)

"""
ala ma kota
ala ma tez psa
print(x)
print("ala")
"""

##################################

price = 19.99
age = 20

print(age)
print(price)
age = 30.0
print(age)

#################################

x = 5
y = x + 5 # y -> 10

print(y)

x1 = 10
x1 = x1 + 1 # 11
print(x1)

x1 += 1

#################################

y = "ala"
x = "20"
z = 20
c = 20.3

print(type(x))
print(type(y))
print(type(z))
print(type(c))

razem = x + y
print(razem)

# razem2 = x + z
# print(razem2)

#################################




x = 1.0
y = "str"

print(type(x) == float)

print(isinstance(x, (float, int)))


##################################
x = 7
x = float(7)
print(x)


##################################

var = "ala"
print(var[1])
var = "ala2"
print(var[-1])

x = "python"
print(x[0])
print(x[-1])

print(x[0:3])






x = "Ala ma kota" #0=A, 1=l ...
x = x.upper()
print(x)

name = "Ale"

print(name[-1] == 'a')

############################################

# Ćwiczenie 1
name = input("Podaj imię: ")

print(f"Witaj, {name}")