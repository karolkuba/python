import hashlib
from enum import Enum

from ćwiecznia.pracownicy.model.employee import Employee, Permission
from ćwiecznia.pracownicy.model.trainee import Trainee


class CompanyController:
    employees = [ Employee("mk1","mk1","PYTHON DEV",11000,Permission.ROLE_EMPL),
        Employee("mk2","mk2","JAVA DEV",9000,Permission.ROLE_EMPL),
        Employee("mk3","mk3","PYTHON DEV",12000,Permission.ROLE_EMPL),
        Employee("mk4","mk4","MANAGER",14000,Permission.ROLE_MAN),
        Employee("mk5","mk5","SCRUM MASTER",13000,Permission.ROLE_MAN),
        Employee("mk6","mk6","HEAD",17000,Permission.ROLE_HEAD),
        Employee("mk7","mk7","HEAD",21000,Permission.ROLE_HEAD),
        Employee("mk8","mk8","DEV OPS",11500,Permission.ROLE_EMPL),
        Trainee("t1", "t1"),
        Trainee("t2","t2"),
        Trainee("t3","t3")]


    # 1* sprawdzanie czy dany login nie istnieje w liście employees
    def loginValid(self, login):
        for e in self.employees:
            if(e.login == login):
                return False
        return True

    # 1. dodawanie pracownika lub praktykanta z unikatowym loginem
    def AddEmployeeorTrainee(self, o):
        if(o.__class__.__name__ == "Trainee" or o.__class__.__name__=="Employee"):
            if(self.loginValid(o.login)):
                print("dodano pracownika",o.login, o.password)
                self.employees.append(o)
            else:
                print("istnieje już taki login w naszej bazie danych")
        else:
            print("dany obiekt nie jest pracownikiem ani praktykantem")


     #2. wyświetlenie wszystkich pracowników i praktykantów posortowanych po pensji
    def getEmployees(self):
        # sortowanie po pensji
        for e in sorted(self.employees, key=lambda e : e.salary, reverse = True):
            print(e)


    # 3 wyświetlenie tylko kierowników
    def getMan(self):
        for e in self.employees:
            if(e.__class__.__name__=="Employee"):
                if(e.permission.value==2):
                    print(e)



    #4. wyświetlnie tylko kierowników lub dyrektorów posortowanych po loginia A-Z
    def getTreineeOrderByLogin(self):
        for t in sorted(self.employees, key=lambda t:(t.login and t.__class__.__name__=="Trainee"),
            reverse=True):
                print(t)

    # 5. przypisanie nagrody do pracownika lub praktykanta po loginie, jesli nie podamy loginu to premia dla wszytskich
    def setPrise(self, amount, login = ""):
        if(login != ""):
            islogin = False
            for e in self.employees:
                if(e.login == login):
                    e.assignPrise(amount)
                    islogin = True
                    break
            if(islogin == False):
                print("błędny login pracownika")
        else:
            for e in self.employees:
                e.assignPrise(amount)
        self.getEmployees()

        self.salary = amount




    #  6. zmiana pensji tylko dla pracownika
    def changeEmployeeSalary(self, login, salary):
        isEmployee = False
        for e in self.employees:
            if(e.login==login and e.__class__.__name__ == "Employee"):
                e.salary=salary
                isEmployee = True
                break
        if(isEmployee ==False):
            print("błędny login lub typ pracownika")
        self.getEmployees()

    # 7. usuwanie pracownika lub praktykana
    def deleteEmployeeOrTrainee(self,login):
        isFound = False
        for l in self.employees:
            if(l.login==login):
                isFound = True
                self.employees.remove(l)
                print("usunięto: " , l.login)
        if(isFound == False):
            print("nie ma takiego pracownika")

        # 7**. usuwanie pracownika lub praktykana z potwierdzeniem hasłą

    def deleteEmployeeOrTraineeByLoginWithConfirm(self, login):
        isFound = False
        for e in self.employees:
            if (e.login == login):
                isFound = True
                if (e.password == hashlib.md5(
                        (input("potwierdz usuwanie hasłem")).encode('utf-8')).hexdigest()):
                    self.employees.remove(e)
                    print("Usunięto: ", e.login)
                else:
                    print("Błąd potwierdzenia")
        if (isFound == False):
            print("Nie ma takiego pracownika")
        self.getEmployees()







