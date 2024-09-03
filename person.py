from utils import getPrompt, getNum, getUserInput, getId

class Person:
    def __init__(self, info_dict):
        self._name = getUserInput("persons name")
        self._age = getNum("persons age")
        self._id = getId(info_dict)
        
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def getRole(self):
        return "Person"
    
    def getId(self):
     return self._id

    def setId(self, person_id):
        self._id = person_id
    
    def getPersonInfo(self):
        return (
        "Name: " + self.getName() + "\n" +
        "Age: " + str(self.getAge()) + "\n" +
        "ID: " + str(self.getId()))

    def getFullDetails(self):
        return {
            "id": self._id,
            "name": self._name,
            "age": self._age,
            "role": self.getRole(),
        }
    
if __name__ == "__main__":
    person = Person("timmy", 30, 0)
    if person.getName() == "timmy":
        print("getName() passed")
    else:
        print("getName() failed")
        
    if person.getAge() == 30:
        print("getAge() passed")
    else:
        print("getAge() failed")
        
    if person.getRole() == "Person":
        print("getRole() passed")
    else:
        print("getRole() failed")
        
    if person.getId() == 0:
        print("getId() passed")
    else:
        print("getId() failed")
        
    person.setName("john")
    if person.getName() == "john":
        print("setName() passed")
    else:
        print("setName() failed")
        
    person.setAge(35)
    if person.getAge() == 35:
        print("setAge() passed")
    else:
        print("setAge() failed")
        
    person.setId(1)
    if person.getId() == 1:
        print("setId() passed")
    else:
        print("setId() failed")
        
    expected_info = "Name: john\nAge: 35\nID: 1"
    if person.getPersonInfo() == expected_info:
        print("getPersonInfo() passed")
    else:
        print("getPersonInfo() failed")
    
    expected_details = {
        "id": 1,
        "name": "john",
        "age": 35,
        "role": "Person"
    }

    if person.getFullDetails() == expected_details:
        print("getFullDetails() passed")
    else:
        print("getFullDetails() failed")
    





