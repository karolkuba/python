from ćwiecznia.pracownicy.controller.companyController import CompanyController
from ćwiecznia.pracownicy.model.employee import Employee
from ćwiecznia.pracownicy.model.trainee import Trainee

cc = CompanyController()
# cc.AddEmployeeorTrainee(Employee("e1","e2","Junior DEV", 5000))
# cc.AddEmployeeorTrainee(Employee("e1","e2","Junior DEV", 5000))
# cc.AddEmployeeorTrainee("Pani Jadzia z gazowni")
# cc.AddEmployeeorTrainee(Trainee("p1","p2"))
# cc.getEmployees()
# cc.getMan()
# cc.getTreineeOrderByLogin()
# cc.AddPrize
# cc.setPrise(250, "mk7")
#cc.changeEmployeeSalary("mk1",2230)
#cc.deleteEmployeeOrTrainee("mk2")
cc.deleteEmployeeOrTraineeByLoginWithConfirm("mk3")
