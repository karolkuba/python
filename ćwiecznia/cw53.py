# kwadraty liczb od 3 do 9

for i in range(3,10):
        print("%i ^ 2 = %i" % (i, i**2))


# wygeneruj tablice z przedzialami losowymi od 0 do 10

import random
randomList = []
for i in range(10):
    randomList.append(random.randint(1,10))
print(randomList)

#wyszukaj elementu z listy i zwróć jego indeks
#jeżeli elementu nie ma na liście to zwróc -1
find = int(input("podaj liczbę z zakresu od 1 do 10"))
#sprawdzamy czy element występuje w liście
if(find not in randomList):
    print("element %i nie występuje na liscie" % find)
else:
    for index, value in enumerate(randomList):
        if(value == find):
            print("element %i znajduje się na indeksie %i" % ( find, index))
            break


# sprawdź ile razy  szukany element wystepuje na liście
count = 0
for element in randomList:
    if(element == find):
        count += 1
print("element %i występuje w liście %i razy" % (find, count))