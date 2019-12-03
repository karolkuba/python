from math import sqrt


def calculateDistance(x,y):
    return sqrt(pow(y[0]-x[0],2)+pow(y[1] - x[1],2))

p1 = [-1,-1]
p2 = [1,1]
print(calculateDistance(p2,p1))
