print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.")
print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print()
    print("Length options:")
    print("1 - meter to kilometer")
    print("2 - kilometer to meter")
    print("0 - exit")
    
    choice1 = int(input("Your choice: "))
    
    if choice1 == 1:
        meter = float(input("Insert meter: "))
        kilometer = round(meter / 1000, 1)
        print(f"{meter} m is {kilometer} km")
        
    elif choice1 == 2:
        kilometer = float(input("Insert kilometer: "))
        meter = round(kilometer * 1000, 1)
        print(f"{kilometer} km is {meter} m")
        
    elif choice1 == 0:
        print("Exiting...")
        
    else:
        print("Unknown option.")

elif choice == 2:
    print("\nWeight options:")
    print("1 - grams to pounds")
    print("2 - pounds to grams")
    print("0 - Exit")
    
    choice1 = int(input("Your choice: "))
    
    if choice1 == 1:
        grams = float(input("Insert grams: "))
        pounds = round(grams / 453.592, 1)
        print(f"{grams} g is {pounds} lb")
        
    elif choice1 == 2:
        pounds = float(input("Insert pounds: "))
        grams = round(pounds * 453.592, 1)
        print(f"{pounds} lb is {grams} g")
        
    elif choice1 == 0:
        print("Exiting...")
        
    else:
        print("Unknown option.")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")
print()
print("Program ending.")
