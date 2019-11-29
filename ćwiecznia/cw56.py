def isGrade(grade):
    return grade in gradesTemplate
def gradesAvg(grades):
    sum=0
    for grade in grades:
        sum+= grade
    return sum/len(grades)

gradesTemplate = (3.0,3.5,4.0,4.5,5.0)
grades = []
while(True):
    grade = input("wprowadź ocenę (ENTER-wyjście)")
    if(grade == ""):
        print("średnia ocen: %.2f" % gradesAvg(grades))
        break
        # sprawdzanie typu danych
    try:
        grade = float(grade)
    except:
        print("ocena musi być liczbą!")
        # sprawdzenie czy wartośc liczbowa jest na skali ocen
    if(not isGrade(grade)):
        print("nie ma takiej oceny w skali ocen")
        continue
    grades.append(grade)
    print("wprowadzone oceny: %s " % grades)