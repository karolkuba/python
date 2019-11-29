list = [4,5,3,2,1,6]
index = int(input("podaj element od 1 do 6: " + str(list))) - 1

if (index >= 0 and index < len(list)):
    print("Twój wybór: ", list[index])
else:
    print("out of range")

#47
# czy dwa pierwsze elementy listy  są dodatnie

if(list[0] >= 0 and list[1] >= 0):
    print("dwa pierwsze elementy są dodatnie")
elif(list [0] > 0 and  list[1] <= 0):
    print("tylko pierwszy element jest dodatni")
elif(list[0]<= 0 and list[1]>0):
    print("tylko drugi element jest dodatni")
else:
    print("oba elementy są ujemne")

#cw48
# sprawdz czy wprowadzona liczba jest parzysta
print("wprowadzona wartość jest: ", "parzysta" if ((index+1)% 2 == 0) else "nieparzysta")

