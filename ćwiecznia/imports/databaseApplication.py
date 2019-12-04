# importy są adresowane od katalogu domowego -> do naszego projektu
# nazwa skryptu modułu występuje bez rozszerzenia
# alias zastępuje wszystko co jest w adresie modułu razem z jego nazwą

# import ćwiecznia.imports.SecretVariables as sv
#
# for i in dir(sv):
#     print(i)

#help(sv)


# # dostęp do zmiennych
# print(sv.database)
# print(sv.username)
# print(sv.password)
# print(sv.port)
# print(sv.host)
#
# # dostęp do metod
# print(sv.getConnection())
#
# #dostęp do klas
# obiektKlasyZaimportowanej = sv.Hello("Michał")
# print(obiektKlasyZaimportowanej)
# print(obiektKlasyZaimportowanej.name)

import os
print("Direct ref",os.getcwd())

print("w katalogu w którym znajdujemy się aktualnie: ")
for i in os.listdir('.'):
    print(i)

print("w katalogu pracownikow jest cos takiego:")
for i in os.listdir("C:\\Users\\dell\\PycharmProjects\\python\\ćwiecznia\\pracownicy"):
    print(i)