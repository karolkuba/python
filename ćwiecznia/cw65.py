from random import randint


def generateRandomElements(n):
    elements=[]
    for i in range(n):
        elements.append(randint(-1000,1000))
    print(elements)
    return elements


def getElementsSupportTreshold(n,treshold):
    elementsSupportTreshold = []
    cumSum=0
    for elem in generateRandomElements(n):
        if(elem > treshold):
            cumSum+=elem
            elementsSupportTreshold.append(elem)
    return elementsSupportTreshold, cumSum

#print(generateRandomElements(10))
print(getElementsSupportTreshold(10,500))