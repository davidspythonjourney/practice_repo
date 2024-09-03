import json
import re
import pandas as pd
from employee import Employee
from person import Person
from student import Student
from enums import MenuOption
from utils import *

def checkIfEmpty(data_dict):
    if not data_dict:
        print("The dictionary is empty.")
        return True
    return False

def saveNewEntry(data_dict: dict, avg_dict: dict):
    class_map = {
        "student": Student,
        "employee": Employee,
        "person": Person
        }
    while True:
        role = input(getPrompt("Enter your role (" + ', '.join(class_map.keys()) + ")")).lower()
        if role in class_map:
            person = class_map[role](data_dict)
            data_dict[person.getId()] = person
            avg_dict["total_age"] += person.getAge()
            avg_dict["num_entries"] = len(data_dict)
            print("Entry with ID: " + str(person.getId()) + " added successfully")
            break
        else:
            continue

def searchId(id_num: int, data_dict):
    if checkIfEmpty(data_dict):
        return
    if checkId(data_dict, id_num):
        person = data_dict[id_num]
        print(formatPersonDetails("", person))
    else:
        print("No ID: " + str(id_num) + " was found!")
             
def avgAges(avg_dict):
    if avg_dict["num_entries"] == 0:
        print("The average is: 0")
    else:
        print("{:.2f}".format(avg_dict["total_age"] / avg_dict["num_entries"]))
        
def showAllIds(data_dict):
    if checkIfEmpty(data_dict):
        return
    for index, person_id in enumerate(data_dict.keys()):
        print(str(index) + ". " + str(person_id))
                   
def showName(data_dict):
    if checkIfEmpty(data_dict):
        return
    for index, person in enumerate(data_dict.values()):
        print(f"{index}. {person.getName()}")

def showAll(data_dict):
    if checkIfEmpty(data_dict):
        return
    for index, (person_id, person) in enumerate(data_dict.items()):
        print(formatPersonDetails(f"{index}.", person))
                  
def validateIndex(data_dict):
    if checkIfEmpty(data_dict):
        return
    while True:
        index = getNum("index")
        if 0 <= index < len(data_dict):
            return index
        else:
            print(f"Index out of range - index range is: 0 - {len(data_dict) - 1}")
                      
def printEntryByIndex(index, data_dict):
    if checkIfEmpty(data_dict):
        return
    for index_val, (person_id, person) in enumerate(data_dict.items()):
        if index_val == index:
            print(formatPersonDetails(f"{index}. ", person))
                       
def options():
    for option in MenuOption:
        print(f"{option.value}. {option}")
    while True:
        choice = getNum("your choice")
        try:
            selected_option = MenuOption(choice)
            print(f"You selected option {selected_option}")
            return selected_option
        except ValueError:
            print(f"Invalid choice. Please select a number between {MenuOption.min_value} and {MenuOption.max_value}.")
            
def getColumnNamesFromConfig():
    with open("conf.json", "r") as f:
        return json.load(f)
        
def getFileName():
    while True:
        file_name = input("Please enter your desired file name (without .csv or any special characters): ")
        if file_name and not file_name.endswith('.csv') and not file_name.endswith('.'):
            if re.match("^[A-Za-z0-9._-]+$", file_name):
                return file_name + ".csv"
            print("Please enter a valid file name in the requested format.")

def getOutputFileInfo(data_dict):
    if checkIfEmpty(data_dict):
        return None
    return [person.getFullDetails() for person in data_dict.values()]

def createCsv(data):
    if not data:
        return  
    file_name = getFileName()
    output_df = pd.DataFrame(data)  
    output_df.to_csv(file_name, index=False)

def start():
    user_dict = {}
    avg_dict = {'total_age': 0, 'num_entries': 0}
    while True:
        chosen_option = options()
        if chosen_option == MenuOption.SAVE_NEW_ENTRY:
            saveNewEntry(user_dict, avg_dict)
        elif chosen_option == MenuOption.SEARCH_BY_ID:
            id_num = getNum("ID")
            searchId(id_num, user_dict)
        elif chosen_option == MenuOption.PRINT_AGES_AVERAGE:
            avgAges(avg_dict)
        elif chosen_option == MenuOption.PRINT_ALL_IDS:
            showAllIds(user_dict)
        elif chosen_option == MenuOption.PRINT_ALL_NAMES:
            showName(user_dict)
        elif chosen_option == MenuOption.PRINT_ALL_ENTRIES:
            showAll(user_dict)
        elif chosen_option == MenuOption.PRINT_ENTRY_BY_INDEX:
            index = validateIndex(user_dict)
            if index is not None:
                printEntryByIndex(index, user_dict)
        elif chosen_option == MenuOption.SAVE_ALL_DATA:
            info = getOutputFileInfo(user_dict)
            if info:
                createCsv(info)
        elif chosen_option == MenuOption.EXIT:
            print("Good-Bye")
            break
        try:
            input("Press Enter to continue...")
        except (KeyboardInterrupt, EOFError) as uh_oh:
            print("\nError occurred: ", uh_oh)
            print("Continuing...")
            
    
if __name__ == "__main__":
    start()

