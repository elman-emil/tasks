def options():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
def choice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    print("Unknown option!\n")
    return -1
def main():
    print("Program starting.")
    count = 0
    while True:
        options()
        choices = choice()
        if choices == 1:
            print(f"Current count - {count}\n")
        elif choices == 2:
            count += 1
            print("Count increased!\n")
        elif choices == 3:
            count = 0
            print("Cleared count!\n")
        elif choices == 0:
            print("Exiting program.\n")
            break
        elif choices == -1:
            continue
        else:
            print("Unknown option!\n")
    print("Program ending.")


main()