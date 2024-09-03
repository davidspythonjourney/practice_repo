from person import Person
from utils import *

class Student(Person):
    def __init__(self, info_dict):
        super().__init__(info_dict)
        self._field_of_study = getUserInput("student's field of study")
        self._average_score = getNum("student's average score", True)
        self._grade = getNum("student's grade", True)
        self._year_of_study = getNum("student's year of study")

    def getFieldOfStudy(self):
        return self._field_of_study

    def getYearOfStudy(self):
        return self._year_of_study

    def getAverageScore(self):
        return self._average_score
    
    def getGrade(self):
        return self._grade
    
    def getRole(self):
        return "Student"

    def getPersonInfo(self):
        return super().getPersonInfo() + ", Role: " + self.getRole() + \
               ", Field of Study: " + self._field_of_study + \
               ", Average Score: " + str(self._average_score) + \
               ", Grade: " + str(self._grade) + \
               ", Year of Study: " + str(self._year_of_study)
               
    def getFullDetails(self):
        details = super().getFullDetails()
        details.update({
            "field_of_study": self._field_of_study,
            "average_score": self._average_score,
            "grade": self._grade,
            "year_of_study": self._year_of_study
        })
        return details

    
if __name__ == "__main__":
    student = Student("Jimmy", 20, 770, "Computer Science", 85.5, 60, 2)
    if student.getFieldOfStudy() == "Computer Science":
        print("getFieldOfStudy() passed")    
    else:
        print("getFieldOfStudy() failed")
        
    if student.getYearOfStudy() == 2:
        print("getYearOfStudy() passed")
    else:
        print("getYearOfStudy() failed")
        
    if student.getAverageScore() == 85.5:
        print("getAverageScore() passed") 
    else:
        print("getAverageScore() failed")
        
    if student.getGrade() == 60:
        print("getGrade() passed")
    else:
        print("getGrade() failed")
        
    if student.getRole() == "Student":
        print("getRole() passed")
    else:
        print("getRole() failed")
        
    expected_info = "Name: Jimmy\nAge: 20\nID: 770, Role: Student, Field of Study: Computer Science, Average Score: 85.5, Grade: 60, Year of Study: 2"
    if student.getPersonInfo() == expected_info:
        print("getPersonInfo() passed")
    else:
        print("getPersonInfo() failed")
        
    expected_details = {
    "id": 770,
    "name": "Jimmy",
    "age": 20,
    "role": "Student",
    "field_of_study": "Computer Science",
    "average_score": 85.5,
    "grade": 60,
    "year_of_study": 2
    }
    if student.getFullDetails() == expected_details:
        print("getFullDetails() passed")
    else:
        print("getFullDetails() failed")
        
    
