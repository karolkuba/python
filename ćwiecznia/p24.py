a = 0
b = 0
c = 1


#warstwa and

andGate1 = (not a) and (not b) and not(c)
andGate2 = (not a) and (not b) and (c)
andGate3 = (not a) and (b) and not (c)
andGate4 = (a) and (not b) and not (c)

# warstwa or
orGateResult = andGate1 or andGate2 or andGate3 or andGate4

print(orGateResult)