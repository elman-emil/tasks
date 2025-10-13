print("Program starting.")
print()
print("Options:")
print("1 -- Celsius to Fahrenheit")
print("2 -- Fahrenheit to Celsius")
print("0 -- Exit")

choice = int(input("Your choice: "))

if choice == 1:
    temp_c = float(input("Insert the amount of Celsius: "))
    temp_f = (temp_c * 1.8) + 32
    print(f"{round(temp_c, 1)} °C equals to {round(temp_f, 1)} °F")

elif choice == 2:
    temp_f = float(input("Insert the amount of Fahrenheit: "))
    temp_c = (temp_f - 32) / 1.8
    print(f"{round(temp_f, 1)} °F equals to {round(temp_c, 1)} °C")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print()
print("Program ending.")
