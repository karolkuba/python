#baza danych

productsNames = "chleb", "mleko", "cukierki"
productPrices = 1.99, 2.50, 12.99
productsQuantity = "sz.", "l", "kg"


# zamówienie

productOrder = 2, 0.5, 0.3

# prezentacja zamówienia

print(productsNames[0], productOrder[0], productsQuantity[0], sep="\t\t")
print(productsNames[1], productOrder[1], productsQuantity[1], sep="\t\t")
print(productsNames[2], productOrder[2], productsQuantity[2], sep="\t\t")


# kwota do zapłaty
print ("SUMA",
       round(productPrices[0] * productOrder[0] +
       productPrices[1] * productOrder[1] +
       productPrices[2] * productOrder[2],2),"zł")



