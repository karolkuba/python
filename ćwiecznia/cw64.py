# funkcja odwołująca się do obiektu globalnie zadeklarowanego w skrypcie


def returnColour():
    global value          # pobierm wartosc globalną
    value=not value   # modyfikuję wartość globalną
    return "black" if value else "white";

value=True
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())