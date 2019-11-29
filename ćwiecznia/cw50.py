
Products = {"1": ["A",3.5, 10],
            "2": ["B",2.99, 5],
            "3": ["C",9.99, 1]
            }
# koszyk zawiera listy zamówionych produktów
basket=[]
cumSum=0
# CLI użytkownika
while(True):
    # pętle wypisująca produkty
    print("| %3s | %10s | %4s[zł] | %5s |" %
        ("ID", "NAZWA".center(10), "CENA", "ILOŚĆ"))
    for key in Products.keys():
        print ("| %3s | %10s | %8.2f | %5.f |" %
              (key, Products[key][0].center(10), Products[key][1],Products[key][2]))
    #pobieranie danych od użytkownika
    choice = input("Co chcesz zamówić podaj id produktu lub Q-wyjście")
    # wyjście z programu
    if(choice.upper() == "Q"):
        break
    if(choice not in Products.keys()):
        print("niepoprawne id")
        continue
    quantity = float(input("wprowadź ilość zamawianego produktu"))
    if(quantity>Products[choice][2] and quantity > 0):
        print("dostępnych jest tylko: "+ str(Products[choice][2]) + "szt.")
        continue
    #aktualizacja magazynu i koszyka
    Products[choice][2] -= quantity #products[choice][2] = products[choice][2] - quantity
    basket.append([Products[choice][0],Products[choice][1], quantity])

    #suma skumulowana zamówień w koszyku
    cumSum += quantity * Products[choice][1]
    print ("Twój koszyk: ", basket)
    print("suma do zapłaty:", cumSum, "zł")



