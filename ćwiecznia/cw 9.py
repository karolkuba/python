#salaryNet = float(input("Wprowadź wynagrodzenie netto: "))
#print (salaryNet * 1.23)

netValue = float(input("Wprowadź kwotę brutto:"))

tax3 = 0.03
tax8 = 0.08
tax23 = 0.23
print(round(netValue,2), "zł brutto to", round(netValue / (1 + tax3),2), "zł netto")
print(round(netValue,2), "zł brutto to", round(netValue / (1 + tax8),2), "zł netto")
print(round(netValue,2), "zł brutto to", round(netValue / (1 + tax23),2), "zł netto")


