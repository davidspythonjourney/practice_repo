import re

def getPrompt(text: str):
    return "Please enter " + text + ": "

def getUserInput(text):
    while True:
        user_input = input(getPrompt(text))
        if user_input and re.match("^[A-Za-z]+$", user_input ):
            return user_input
        print("Please enter a valid " + text + " with characters (not empty).")
        
def getNum(prompt_text, is_float=False):
    while True:
        num = input(getPrompt("your " + prompt_text))
        if is_float:
            try:
                return round(float(num), 2)
            except ValueError:
                print(getPrompt("a valid float for " + prompt_text))
        else:
            if num.isdigit():
                return int(num)
            else:
                print(getPrompt("a valid integer for " + prompt_text))
                
def formatPersonDetails(text, person):
    person_info = person.getPersonInfo()  
    if text:
        return f"{text} {person_info}"
    return person_info
   
def checkId(data_dict, id_num):
    if not data_dict:
        return False
    return id_num in data_dict

def getId(data_dict):
    while True:
        id_num = getNum("ID")
        if checkId(data_dict, id_num):
            existing_entry = data_dict[id_num]
            print(formatPersonDetails("An entry already exists with the entered ID:", existing_entry))
            print("Please provide a different ID.")
        else:
            return id_num