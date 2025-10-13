print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print()
print("Options: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

Choice = int(input("Your choice: "))
if Choice == 1:
    print(f"Welcome {name}!")
elif Choice == 2:
    print(f"{name[::-1]}")
elif Choice == 3:
    print(f"The first character in the name ",{name}," is ",{name[0]},"")

    



   