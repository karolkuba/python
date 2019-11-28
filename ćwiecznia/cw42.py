from random import sample

# losuje bez zwracania z populacji - listy wartości, określoną w argumencie liczbę razy

population = range(1,50)
quantity = 6
result = sample(population, quantity)
print(result)
result.sort()   #sortowanie
print(result)

# lub sortowanie
result.sort(reverse=True) #true od najw do najm, false odwrotnie
print(result)
