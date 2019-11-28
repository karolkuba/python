decimalToRoman = {
    0:"0", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V" }

decNum = input("podaj cyfrę w systemie dziesiętnym: ")
if(decNum.isdecimal()):
    decNum = int(decNum)
    if(decNum >= 0 and decNum <= 5):
        print(decimalToRoman[int(decNum)])
    else:
        print("liczba jest spoza zakresu 0-5")
else:
    print("błędne dane")