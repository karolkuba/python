'''
elements = [1,2,3,4,5,6,7]
index = 0
while(True):
    print(index, elements[index])
    index += 1                          #inkrementacja indeksu
    if(index == len(elements) - 1):     # warunek przerwania
        break;                          # przewanie zakańcza działanie pętli
'''

'''
elements = range(5,50,1)
index = 0
while(True):
    print(index, elements[index])
    index += 1                          #inkrementacja indeksu
    if(index == len(elements) - 1):     # warunek przerwania
        break;
'''

# wprowadź dane z klawiatury tak długo aż użytkownik wpisze Q

elements = []
while(True):
    elem = input("podaj wartość lub wprowadź Q zeby wyjść")
    if(elem.upper() == "Q"):
        print("wyjście")
        break
    elements.append(elem)
print(elements)













