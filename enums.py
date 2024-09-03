from enum import Enum

class MenuOption(Enum):
    SAVE_NEW_ENTRY = 1
    SEARCH_BY_ID = 2
    PRINT_AGES_AVERAGE = 3
    PRINT_ALL_IDS = 4
    PRINT_ALL_NAMES = 5
    PRINT_ALL_ENTRIES = 6
    PRINT_ENTRY_BY_INDEX = 7
    SAVE_ALL_DATA = 8
    EXIT = 9
    
    def __str__(self):
        return self.name.replace('_', ' ').title()
    
    @classmethod
    def min_value(cls):
        return min(member.value for member in cls)

    @classmethod
    def max_value(cls):
        return max(member.value for member in cls)
    
if __name__ == "__main__":
    if MenuOption.min_value() == 1:
        print("min_value() passed")
    else:
        print("min_value() failed")
    
    if MenuOption.max_value() == 9:
        print("max_value() passed")
    else:
        print("max_value() failed")
        
    if str(MenuOption.SAVE_NEW_ENTRY) == "Save New Entry":
        print("SAVE_NEW_ENTRY passed")
    else:
        print("SAVE_NEW_ENTRY failed")

    if str(MenuOption.EXIT) == "Exit":
        print("EXIT passed")
    else:
        print("EXIT failed")