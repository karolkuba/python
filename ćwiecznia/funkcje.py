# funkcja zwracająca kolejną liczbę pierwszą względem zadanej wartości
# l pierwsze 1,3,4,7,11 ....
# 5 z kolei (n) -> 11



def getPrimaryNumbers(n):
    primaryNumbers = [1]
    number=2

    while(len(primaryNumbers) <= n):
        isPrimary = True
        for div in range(2,number):
            if(number % div == 0):
                isPrimary = False
        if(isPrimary):
            primaryNumbers.append(number)
        number += 1
    return primaryNumbers, primaryNumbers[len(primaryNumbers)-1]

 #wywołanie funkcji
element = 11
print("Lista: ", getPrimaryNumbers(element)[0])
print(element, "element:", getPrimaryNumbers(element)[1])


############## kolejny przykład ##########################
from datetime import date, datetime, time


def printParameters(login,password,email, status=True, registrationDate=date.today()):
    return ("%s %s %s %s %s" % (login, password, email, status, registrationDate))

# różne wywołania
print(printParameters("mk","mk","mk"))  #tylko argumenty obowiązkowe
print(printParameters("mk1","mk1","mk1", registrationDate="2020-01-01"))  #argumenty obowiązkowe + wybrany argument opcjonalny
print(printParameters("mk2","mk2","mk2", registrationDate="2020-01-01", status = False))  #wszystkie argumenty

###### funkcja w ktorej nie definiujemy ilosci parametrów

def nonDefinedParameters(*elements):  # parametr gwiazdka -> przyjmuje dowolną liczbę argumentów
    sum = 0
    for elem in elements:
        sum += elem
    return sum/len(elements)
print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,2,2,2))


#################
def sortList(numbers):
    numbers.sort()
    return numbers
list=[3,2,5,4,6]
print(sortList(list))


################ sortowanie liczby w kolejnosci
def bubbleSort(elements):
    noProbes = 1
    # pętle iterująca po kolejnych próbach sortowania
    for probe in range(len(elements)-1):   # determinujemy 5 prób w najgorszym przypadku
        isSorted=True
        for index,value in enumerate(elements):
            if(index == len(elements)-1):
                break
            if(elements[index] > elements[index+1]):     # porównywanie sąsiednich komórek
                isSorted=False
                elem = elements[index+1]                 # wydobycie elementu na indeksie i+1 do zmiennej
                elements[index+1]= elements[index]       # zamiana kolejności
                elements[index]=elem
        print(noProbes,elements)
        if(isSorted):                                    # sprawdzenie czy bylismy w if z zamianą elementów
            break
        noProbes += 1
    return elements
print(bubbleSort([3,2,5,4,6,1]))

################ sortowanie liczby w kolejnosci od największych do najmniejszych
def bubbleSort(elements,asc=True):
    noProbes = 1
    # pętle iterująca po kolejnych próbach sortowania
    for probe in range(len(elements)-1):   # determinujemy 5 prób w najgorszym przypadku
        isSorted=True
        for index,value in enumerate(elements):
            if(index == len(elements)-1):
                break
            if((elements[index] > elements[index+1]) and asc):     # porównywanie sąsiednich komórek
                isSorted=False
                elem = elements[index+1]                 # wydobycie elementu na indeksie i+1 do zmiennej
                elements[index+1]= elements[index]       # zamiana kolejności
                elements[index]=elem
            if ((elements[index] < elements[index + 1]) and not asc):  # porównywanie sąsiednich komórek
                isSorted = False
                elem = elements[index + 1]  # wydobycie elementu na indeksie i+1 do zmiennej
                elements[index + 1] = elements[index]  # zamiana kolejności
                elements[index] = elem
        #print(noProbes,elements)
        if(isSorted):                                    # sprawdzenie czy bylismy w if z zamianą elementów
            break
        noProbes += 1
    return elements

import time
print(bubbleSort([3,2,5,4,6,1]))
t_start=time.time()
print(bubbleSort([3,2,5,4,6,1], asc = False))
t_stop=time.time()
print("czas wykonania funkcji: ", t_stop-t_start)

