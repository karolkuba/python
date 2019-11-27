# CTRL + / -komentarz


print('Witaj w Pythonie')

# zmienne -> deklaracja i przypisanie -> inicjalizacja zmiennej (obiektu)

text = "Witaj"
name = "Michał"
sign = 'a'
print(text + " " + name)

# zmienne na podstawie innych zmiennych
a = 1
b = a + 1
print(a, b, (a * b))

print(a, end=';')
print(b , end=';')
print(a + b, end='\n')    # /n -newline
print('www.xyz.pl\\all')
print('"Cytat"')
print("I'm Michał")
print("\"Cytat\"")

# usuwanie obiektu z pamięci podręcznej
del(a)
# print(a) -> name 'a' is not defined

# zad 1

a = 1
b = 2.4
c = "w1"
print(a, b, c, sep='\t\t')

# zad 2
a = 2.1
b = "abc"
c = 0
print(a, b, c)

#zad 3

a = 13
b = c

print(a,b,c)

#zad 4

del(a)
del(c)
c = 31.3
# print(a,b,c) -> a is not defined

'''
name = input("Podaj imię:")   # input zwraca stringa (typ napisowy)
lastname = input("Podaj nazwisko: ")
birthDate = input("Podaj datę urodzenia (YYY-MM-DD): ")
possition = input("Podaj stanowisko")
salaryNet = float(input("Wprowadź wynagrodzenie netto")) # konwersja string ->
print(name, lastname, birthDate, possition, str(salaryNet) + "zł",str(salaryNet * 1.23) + "zł", sep=' | ')
'''


and1 = 1
print(and1)

# typy zmiennych
name = "Michał"
salary = 1000.
isActivated = True
element = 1
print(type(name), type(salary), type(isActivated), type(element))

# liczby zespolone

complexNum1 = 2 + 2j
complexNum2 = 5j
realNum1 = 2
print(complexNum1 + complexNum2)
print(complexNum1 * realNum1)
print(type(complexNum1))

# operacje na liczbach

num1 = 1
num2 = 2
print(1/2)
print(1//2) # wymusza obcięcie przecinka

print(round(1.2,3))

# konwersja rozszerzająca i zawężająca

print(int(1.9999)) # konwersja zawężająca

intNum = 5
print(float(intNum)) # konwersja roszerzająca


# typ logiczny
print(bool(121),bool(0))
print(bool("dead"),bool(""))
print(bool(12.2),bool(0.))
print(bool((1,2,3)), bool ( () ))


#string

name= "Michał"
print(len(name))  # string to ciąg znaków występujących na określonych pozycjach
print(name[0])
print(name[len(name) - 1])

name = name + " " + "KRUCZKOWSKI"
print("ADD: " + name)
name = name[0:6]
print ("SUB: " + name)


print(8 ** (1/3))
print(8 ** (0.33))

x=1 # przypisanie wartości do obiketu
x == 1 # porównanie wartości przyjmowanej przez obiekt x z licxzbą jeden

# print(x = 1) błąd
print(x==1)

# porównanie leksykograficzne - CZY JEST leksykograficzne mniejszy czy wiekszy - po kodzie asci

name1 = "ala"
name2 = "Ala"

print("==",name1 == name2)
print(">",name1>name2)

print(ord('a'), ord('A'))
print(ord('a'), ord('n'))







