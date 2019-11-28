sentence =  "Ala ma kota, a kot ma Ale."
# oczyść zdanie ze znaków interpunkcyjnych
sentence=sentence.replace(".","")
sentence=sentence.replace(",","")
print(sentence)

words=sentence.split(" ")
print(words)


# listy

params = []
row = [1,"Adam","Nowak","2000-01-01",True, 5500.]

# dodawanie parametrów do params
params.append(12.5)
params.append(11.5)
params.append(9.4)

# wypisanie elementów listy
print(params)
print(row)

# zmiana pensji w liście row
row[5]= 6000.
print(row)
print (row[1:3])
print (row[0:5:2]) # co drugi
print(row[1:]) # od drugiego do konca
print(row[:3])  # print pierwsze trzy włącznie
print(row[::-1]) # odwrtona kolejność włącznie indeks 0

#powielanie list
row=row*2
print(row)
#row *= 0 # row= row*0 czysci liste
#print(row)

# długość listy
print(len(row))

row[6:]=[2,"Jan","Kowalski","2011-02-12",False,10000]
print(row)


#operator przynależności
print("Kowalski" in row)
print("Kowalski" not in row)


name = "Michał"            #niezmienny
#name[3]='k'

#konwersja na listę
name = list(name)          #edytowalny
name[3]='k'
print(name)

string = ""
for v in name:
    string += str(v)
print(string)              #niezmienny

name =str(name)               # drugi sposób na złączenie listy
name = name.replace("'","")
name = name.replace(", ","")
name = name.replace("]","")
name = name.replace("[","")
print(name)

#usuwanie elementów listy
numbers = [1,2,3,4,5]
numbers.remove(3)        # usuwa po wartości
print(numbers)
deleted = numbers.pop(2) # usuwa po indeksie ze zwracaniem wartości
print(numbers)
print(deleted)


# sprawdź czy dwa napisy są palindromami (są lustrzane) - CZĘSTO NA REKTRUTACJI

# I SPOSOB
text = "kajak"
print(text[:] == text[ : :-1])

# DRUGI SPOSOB
text=list(text)
textRev = text
textRev.reverse()
print(text == textRev)

#sortowanie
nums = [1.1, 2.1, 0.15, 15., 1., 4., 5.]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

names = ["Ala","Ola","Ela"]
names.sort()
print(names)

# LISTY WIELOWYMIAROWE
kik = [
    ["","",""],
    ["","",""],
    ["","",""]
     ]
print(kik)
print(len(kik))
print(len(kik[0]))
print(len(kik[1]))
print(len(kik[2]))
kik[2][2] = "X"
print(kik)
kik[1][0:2] = ["O","O"]
print(kik)

#dodanie listy do listy kik od tyłu
kik.append(["*","*","*"])
print(kik)

#dodanie listy do listy kik od przodu
kik.insert(0,["*","*","*"])
print (kik)
print(len(kik))


############################ KROTKI #######################
tupleType = (1,2,3,4,5)
# tupleType[1] = 55   -> krotka jest typem niezmiennym

multiDimTuple = ([1,2],[3,4],[5,6])
print(multiDimTuple)
# multiDimTuple[0] = 1 -> nie mozna edytowac krotki

multiDimTuple[0].append('X')
multiDimTuple[0][0] =2
print(multiDimTuple)           # -> można edytować listę w krotce


########################### SŁOWNIKI ########################

products = {}

# dodawanie nowego produktu
products["321321"] = "Pamięć RAM 8GB"
products["123421"] = "Pamięć RAM 16 GB"
products["235124"] = [1,"PC", " Intel i5 8 gen", 700]
print(products)

# modyfikacja pamięci ram

products["321321"] += " NEW" # dodalismy napis do istniejącego
print(products)
print(products.keys())
print(products.values())





################ ZBIORY#######################

A = set([1,2,3,4,5,6])
B = set([4,5,6,7,8])

print("suma", A | B)
print("część wspólna", A & B)
print("różnica A-B", A - B)
print("różnica B-A", B - A)
print("różnica symetryczna", B ^ A)


# dla zdania wprowadzonego przez użytkownika sprawdź ile jest unikatowych słów
# zakładamy ze w zdanie nie występują znaki interpunkcyjne

sentence = input("podaj zdanie")
words = sentence.split(" ")
uniqueWords = set(words)
print("ilość unikatowych słów: ", len(uniqueWords))
print("ilość powtórzeń słów: ", len(words) - len(uniqueWords))








































