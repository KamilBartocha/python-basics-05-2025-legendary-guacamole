list1 = [1, 2, 3, 4]
x = 1
y = 2


try:
    print(list1[3])
    z = x + y
    # open('s.txt')
except IndexError:
    print("Niepoprawny index")
except TypeError:
    print("dodawanie złych zmiennych")
except Exception as err:
    print("Coś poszło nie tak")
else:
    print("nie było nic źle, jest git, dobrze chłopaki robią pozdrawiam Legnicę")
finally:
    print("koniec bloku try/except")


print("dalsza część programu!")
