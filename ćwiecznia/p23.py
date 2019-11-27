
p = False
q = False
result00 = not(p and q) == (not p) or (not q)


p=False
q=True
result01 = not(p and q) == (not p) or (not q)

p=True
q=False
result10 = not(p and q) == (not p) or (not q)


p=True
q=True
result11 = not(p and q) == (not p) or (not q)

print("IS TAUTOLOGY?")
print(result00, result01, result10, result11)