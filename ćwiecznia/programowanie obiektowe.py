# przykład
from datetime import date


class Auto:
    #klasa moze zawierać:

    # pola klasowe -> obiekty, zmienne
    brand = "b/d"
    model = "b/d"
    #metody klasowe -> funkcje

    def helloInClass(self):
        return "Witaj w programowaniu obiektowym"

# utworzenie obiketu
a = Auto()
print(a.helloInClass())
a.brand = "BMW"
a.model = "X3"

print(a.brand,a.model)

a1 = Auto()
print(a1.brand,a1.model)





class User:
    def __init__(self, login, password, status,registrationDate): # metoda wywołana jako pierwsza po utworzenie obiektu
        #pole klasowe są inicjalizowane wartościami z argumentu funkcji
        self.login = login
        self.password = password
        self.status = status
        self.registrationDate = registrationDate

def setStatus(self, status): #modyfikacja statusu na wartość podaną w argumencie
    self.status = status

# funkcje spejalne - wsyztskie te rozpoczynające się od _

def _str_(self): # funkcja wywoływana gdy obiekt jest rzutowany do napisu
    return ("|%10s| %10s| %8s | *10s |" % (self.login,self.password,self.status,self.registrationDate))




u1 = User("mk@mk.pl","mk",True,date.today())
print(u1.login,u1.password,u1.status,u1.registrationDate)
print(u1)

u2 = User("kk@kk.pl","kk",False,date.today())
print(u2.login,u2.password,u2.status,u2.registrationDate)
print(u1)

# cos nie dziala wez od michala


print(u1.__class__.__name__)
print(type(u1))










