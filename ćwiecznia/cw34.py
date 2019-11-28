lin=[
    [],
    []
]
print(lin)

lin[0].append(1)
lin[0].append(2)
lin[0].append(3)

lin[1].append("Adam")
lin[1].append("Ewa")
print(lin)

lin[0].append(int(input("podaj wartość: ")))
lin[0].append(int(input("podaj wartość: ")))
lin[0].append(int(input("podaj wartość: ")))

lin[1].append(input("podaj imię:" ))
lin[1].append(input("podaj drugie imię:" ))
print(lin)