# import z określonej lokalizacji konkretnych składowych
# składowe są dostępne bez adresowania
# SKŁĄDOWE SĄ IMPORTOWANE TYLKO PO NAZWACH


from ćwiecznia.imports.SecretVariables import database, username, password
from ćwiecznia.imports.SecretVariables import getConnection
from ćwiecznia.imports.SecretVariables import Hello

# CTRL +ALt +o -> optimize import, wszystko czego się nie wykorzystuje zostanie usunięte
print(username)
print(database)
print(password)
#print(port) -> nie jest importowane
print(getConnection())
h = Hello("MK")
print(h)