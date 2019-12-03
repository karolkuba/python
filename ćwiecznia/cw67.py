##################### program dziekanat #########################
# -> klasa modelu Student: index, name, lastname, grades[]
# -> klasa logiki biznesowej -> addStudent, getStudents(), deleteStudentByIndex()
# metoda uruchumieniowa -> GUI / CLI



# klasa modelu determinuje strukturę danych
# wspiera podejście ORM - Object Relationship Mapping
# rzutuje cechy danych pochodzące z tabelki sql na obiekt python
import datetime


class Student:
    # konstruktor klasy
    def __init__(self, index, name, lastname, grades =[]):
        self.index = index
        self.name = name
        self.lastname = lastname
        self.grades = grades

    # metoda do dodawania ocen do listy grades
    def addGrade(self, grade):
        self.grades.append(grade)

    # metoda zwracająca średnią ocen
    def calculateAVG(self):
        cumSum=0
        #zabezpieczanie przed dzieleniem przez 0
        if(len(self.grades) == 0):
            return 0
        for grade in self.grades:
            cumSum += grade
        return cumSum / len(self.grades)

    # metoda rzutująca
    def __str__(self):
        return "| %s | %15s | %15s | %20s | %7s |"  %\
               (self.index,self.name,self.lastname,self.grades,"brak danych" if self.calculateAVG() == 0 else round(self.calculateAVG(),2))

# testowanie modelu
# s = Student(123123,"test","test1")
# print(s)
# s.addGrade(5)
# s.addGrade(2)
# s.addGrade(3)
# print(s)

##################################################################################################################

# Kontroller -> klasa obsługi rządań użytkownika pochodzących z widoku [html,cli,window]
# implementuje logikę aplikacji

class StudentController:
    students = []

    # konstruktor -> pobranie i aktualizacja listy z pliku
    def __init__(self):
        inputFile = open("database.csv","r") # otwarcie pliku do odczytu
        for index, line in enumerate(inputFile.readlines()):
            if(index == 0):
                print(line)
                continue
            # każdą linijkę z pliku mapujemy na obiekt student
            rowData = line.split(";")
            #utworzenie obiektu studenta na podstawie danych z jednej lini pliku
            s = Student(rowData[0],rowData[1],rowData[2])
            grades = rowData[3].replace("[","").replace("]","").split(", ")
            # konwersja ocen na float
            print(grades)
            try:
                for index, grade in enumerate(grades):
                    grades[index] = float(grade)
            except:
                grades = []
            #utorzenie obiektu studenta na podstawie danych w jednej lini pliku
            s = Student(rowData[0],rowData[1],rowData[2],grades)
            # zapis zmapowanego obiektu do listy students
            self.students.append(s)
        inputFile.close()                    # zamknięcie strumienia danych do pliku


    # metoda dodająca studenta do listy
    def addStudent(self, index, name, lastname):
        if(self.validateStudentIndex(index)):  # wywołanie walidacji
            # utworzenie obiketu studneta -> odwołanie do modelu
            s = Student(index, name, lastname)
            self.students.append(s)
            print("dodano: ", s)
        else:
            print("istnieje student o wskazanym indeksie")
    # metoda do walidacji danych studenta
    def validateStudentIndex(self,inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                # jezeli juz występuje
                return False # nie dodajemy do lissty
        return True # dodajemy do lissty

    #metoda dodająca ocenę do konkretnego studneta
    def addGradeToStudent(self,inputIndex,grade):
        gradesTemplate = [2,3,3.5,4,4.5,5]
        if(grade in gradesTemplate):
            isAdded = False
            for student in self.students:
                if(student.index == inputIndex):
                    isAdded = True
                    student.addGrade(grade)
                    print("dodano ocenę")
            # wypisz zaktualizowaną listę studentów
            if(isAdded== False):
                print("nie ma studenta o takim indeksie")
            self.getStudents()
        else:
            print("podałeś niepoprawną ocenę")
            self.getStudents()
    def deleteStudentByIndex(self, inputIndex):
        for student in self.students:
            if(student.index == inputIndex):
                print("usunięto", student)
                self.students.remove(student)
        self.getStudents()
    # metoda wypisująca wszystkich studentów z listy studentów
    def getStudents(self):
        print("| %6s | %15s | %15s | %20s | %7s |" % ("INDEKS", "IMIĘ", "NAZWISKO", "OCENY", "ŚREDNIA"))
        for student in self.students:
            print(student)
    def __del__(self):            # destruktor wywołuje się automatycznie gdy niszczony ejst obiekt z pamięci podręcznej
        #otwarcie pliku
        outputFile = open("database.csv","w")
        outputFile.write("data aktualizacji: " + str(datetime.datetime.now()) + "\n")
        #aktualizacja zawartości pliku
        for student in self.students:
            outputFile.write(student.index+";"+student.name+";"+student.lastname+";"+str(student.grades)+
                             ";"+str(student.calculateAVG())+"\n")
        #zamknięcie strumienia danych
        outputFile.close()



'''
#testowanie kontrolera
sc = StudentController()
sc.addStudent(123123, "test", "test1")
sc.addStudent(111111, "test2", "test2")
sc.getStudents()
sc.addGradeToStudent(123123,4)
sc.addGradeToStudent(111111,3)
sc.addGradeToStudent(222222,3)
sc.addGradeToStudent(123123,10)
sc.deleteStudentByIndex(111111)
'''

############## GUI UŻYTKOWNIKA ######################
def CommandLineInterface():
    sc = StudentController()
    while(True):
        try:
            print("aplikacja dziekanat")
            choice = input("(I)- dodaj studenta \n (S) - wypisz studentów \n(G)-dodaj ocenę \n (D)-usuń studenta \n (Q)- wyjście")
            if(choice.upper() == "I"):
                data = input("Podaj numer indeksu, imię i nazwisko ( po spacji)").split(" ") # lista trzech elementów
                sc.addStudent(data[0],data[1],data[2])
            elif(choice.upper() == "S"):
                sc.getStudents()
            elif(choice.upper() == "G"):
                data = input("podaj numer indeksu studenta i oceną która chcesz przypisać(po spacji)").split(" ")
                sc.addGradeToStudent(data[0],float(data[1]))
            elif(choice.upper() == "D"):
                data = input("podaj numer indeksu studenta, którego chcesz usunąć")
                sc.deleteStudentByIndex(data)
            elif(choice.upper() == "Q"):
                print("wyjście")
                break
            else:
                print("błędny wybór")
        except:
            print("ups! coś poszło nie tak")


CommandLineInterface()















