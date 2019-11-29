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

# elements = []
# while(True):
#     elem = input("podaj wartość lub wprowadź Q zeby wyjść")
#     if(elem.upper() == "Q"):
#         print("wyjście")
#         break
#     elements.append(elem)
# print(elements)


# # dana jest lista wartości
# a = [.3, .4, 3.2, 3.5, 1.5, 5.4, 2, 1, 17, 7]
# #napisz program filtrujący wartości po zadanym przez użytkowanika progu
# #tj. na tablicy wynikowej pojawiają się tylko wartości większe od treshold
#
# treshold = float(input("podaj próg odcięcia"))
# result = []
# index = 0
# print(treshold)
# while(index < len(a)):
#     if(a[index] > treshold):
#         result.append(a[index])
#     index+=1
# print(result)
#
# # dwa progi górny i dolny
# tresholdLow = float(input("podaj próg odcięcia dolny"))
# tresholdTop = float(input("podaj próg odcięcia górny"))
# result = []
# index = 0
#
# while(index < len(a)):
#     if(a[index] > tresholdLow and a[index] <tresholdTop):
#         result.append(a[index])
#     index+=1
# print(result)
#
# # przypisanie klas(0 lub 1)
#
# tresholdLow = float(input("podaj próg odcięcia dolny"))
# tresholdTop = float(input("podaj próg odcięcia górny"))
# categorizedResult = []
# index = 0
#
# while(index < len(a)):
#     if(a[index] > tresholdLow and a[index] <tresholdTop):
#         categorizedResult.append(1)
#     else:
#         categorizedResult.append(0)
#     print(a[index], categorizedResult[index])
#     index += 1



# pętla for in

lvls = ["A1","A2","B1","B2","C1","C2"]
for lvl in lvls:
    print(lvl)

for i, lvl in enumerate(lvls):   # enumarate robi indeksy na liscie
    print(i,lvl)

# iterowanie po słownikach w for in

lvlsNames = {lvls[0]: "basic",
             lvls[1]:"basic",
             lvls[2]: "independent",
             lvls[3]: "independent",
             lvls[4]:"proficient",
             lvls[5]: "proficient",
             }
for key in lvlsNames.keys():
    print(key, lvlsNames[key])


