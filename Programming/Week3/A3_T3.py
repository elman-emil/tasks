print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print()

print("Options: ")
print("1 - Print welcome message")
print("0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 1:
    print(f"Welcome {name}!")
elif Choice == 0:
    print("Exiting...")
elif Choice != 1 or 0:
    print("Unknown option.")
print()

print("Program ending.")