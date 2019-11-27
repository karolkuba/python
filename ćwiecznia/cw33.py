# v= spk * (1+p/m)**(n*m)
spk = float(input("podaj kwotę: "))
p = int(input("podaj procent: "))/100
n = int(input("podaj czas trwania lokaty: "))
m = int(input("podaj ilość okresów kapitalizacji"))

print("twój stan konta w przyszłości: ", round(spk*(1+(p/m))**(n*m),2))











#print (float(input("podaj spk: "))) * (1+ float(input))
