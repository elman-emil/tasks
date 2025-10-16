def displayMenu() -> None: # "-> None" doesnt do anything its for the coder to know that the function doesnt do anything here
    print("Menu: ")
    print("1 - View Balance")
    print("2 - Deposit Money")
    print("3 - Withraw Money")
    print("0 - Exit")
    return None 

def getUserChoice():
    UserInput = input("Enter your choice: ")
    return int(UserInput)

def main() -> None:
    print("Welcome to the app.")
    displayMenu()
    choice = -1 
    while choice != 0:
        displayMenu()
        choice = getUserChoice()
    return None

main() 