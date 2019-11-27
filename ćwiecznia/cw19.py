name = input("Podaj imię:")   # input zwraca stringa (typ napisowy)
lastname = input("Podaj nazwisko: ")
birthDate = input("Podaj datę urodzenia (YYY-MM-DD): ")
possition = input("Podaj stanowisko")
salaryNet = float(input("Wprowadź wynagrodzenie netto")) # konwersja string ->
print(name, lastname, birthDate, possition, str(salaryNet) + "zł",str(salaryNet * 1.23) + "zł", sep=' | ')

print("Pan", name, lastname,"(urodzony:", birthDate,")", "pracuje na stanowisku: ",possition, "(pensja:" +str( salaryNet)+")")
