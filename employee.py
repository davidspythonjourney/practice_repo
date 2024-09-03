from person import Person
from utils import getNum, getUserInput

class Employee(Person):
    def __init__(self, info_dict):
        super().__init__(info_dict)
        self._field_of_work = getUserInput("employee's field of work")
        self._salary = getNum("employee's salary", True)

    def getFieldOfWork(self):
        return self._field_of_work

    def getSalary(self):
        return self._salary
    
    def getRole(self):
        return "Employee"

    def getPersonInfo(self):
        return super().getPersonInfo() + ", Role: " + self.getRole() + \
               ", Field of Work: " + self._field_of_work + \
               ", Salary: $" + str(self._salary)

    def getFullDetails(self):
        details = super().getFullDetails()
        details.update({
            "field_of_work": self._field_of_work,
            "salary": self._salary
        })
        return details
    
if __name__ == "__main__":
    employee = Employee("cartmen", 40, 11, "Engineering", 75000)
    if employee.getFieldOfWork() == "Engineering":
        print("getFieldOfWork() passed")
    else:
        print("getFieldOfWork() failed")
        
    if employee.getSalary() == 75000:
        print("getSalary() passed")
    else:
        print("getSalary() failed")
        
    employee.setName("cartmen")
    if employee.getName() == "cartmen":
        print("setName() passed")
    else:
        print("setName() failed")
        
    employee.setAge(45)
    if employee.getAge() == 45:
        print("setAge() passed")
    else:
        print("setAge() failed")
        
    employee.setId(22)
    if employee.getId() == 22:
        print("setId() passed")
    else:
        print("setId() failed")
        
    expected_info = "Name: cartmen\nAge: 45\nID: 22, Role: Employee, Field of Work: Engineering, Salary: $75000"
    if employee.getPersonInfo() == expected_info:
        print("getPersonInfo() passed")
    else:
        print("getPersonInfo() failed")
    
    expected_details = {
    "id": 22,
    "name": "cartmen",
    "age": 45,
    "role": "Employee",
    "field_of_work": "Engineering",
    "salary": 75000
    }
    if employee.getFullDetails() == expected_details:
        print("getFullDetails() passed")
    else:
        print("getFullDetails() failed")
