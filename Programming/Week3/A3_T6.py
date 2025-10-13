print("Program starting.")
print()

print("Main Menu:")
print("1 -- Length")
print("2 -- Weight")
print("3 -- Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print()
    print("Length conversions:")
    print("1 -- Meters to Kilometers")
    print("2 -- Kilometers to Meters")
    sub_choice = int(input("Your choice: "))

    if sub_choice == 1:
        meters = float(input("Insert the amount of meters: "))
        km = meters / 1000
        print(f"{round(meters,1)} m equals to {round(km,1)} km")
    elif sub_choice == 2:
        km = float(input("Insert the amount of kilometers: "))
        meters = km * 1000
        print(f"{round(km,1)} km equals to {round(meters,1)} m")
    else:
        print("Exiting...")

elif choice == 2:
    print()
    print("Weight conversions:")
    print("1 -- Grams to Pounds")
    print("2 -- Pounds to Grams")
    sub_choice = int(input("Your choice: "))

    if sub_choice == 1:
        grams = float(input("Insert the amount of grams: "))
        pounds = grams / 453.59237
        print(f"{round(grams,1)} g equals to {round(pounds,1)} lb")
    elif sub_choice == 2:
        pounds = float(input("Insert the amount of pounds: "))
        grams = pounds * 453.59237
        print(f"{round(pounds,1)} lb equals to {round(grams,1)} g")
    else:
        print("Unknown option.")

elif choice == 3:
    print("Exiting...")

else:
    print("Unknown option.")

print()
print("Program ending.")
