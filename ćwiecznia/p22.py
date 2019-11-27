# 5500 PLN -168H
#  X   PLN - 1H
salaryNet= 5500
hours = 168
zarobki = float(input(" zarobki netto:"))

print("stawka godzinowa netto: ", round(zarobki / hours,2), "PLN/H")
print("stawka godzinowa brutto: ", round(salaryNet * 1.23 / hours,2), "PLN/H")

