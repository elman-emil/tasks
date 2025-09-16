#Task1
print("Hello world!")
print()

#Task2
name1 = 'john'
name2 = 'harry'
print(name1)
print(name2)
print(name1, name2)
print(name1, "is eating ice cream with", name2)
print(name1, "and", name2, "are friends")
print()

#Task3
name = input("What is your name: ")
print("Hi there", name)
print()

#Task4
num1 = 47
num2 = 102
sum = num1 + num2 
diff = num1 - num2 
product = sum * diff
print(f"{num1} + {num2} = {sum}")
print(f"{num2} - {num1} = {diff}")
print(f"{sum} * {diff} = {product}")
print(f"{num1} + {num2} * {num2} - {num1} = {product}")

#Task5 
print("Calculate the area of a wall.")

Feed = input("Enter the width in meters: ")
Width = int(Feed)   


Feed = input("Enter the height in meters: ")
Height = int(Feed)  


print("Width is", Width, "m and height is", Height, "m.")

Area = Width * Height

print("The wall will be", Area, "square meters.")

#Task6
Feed = input("Insert an integer: ")
Value = int(Feed)   
Remainder = Value % 2

print("Value is", Value)
print("The remainder is", Remainder, "when", Value, "is divided by 2.")

#Task7
print("Calculate fuel consumption.")
Feed = input("Enter Travel Distance (Kilometers): ")
Distance = int(Feed)
Feed = input("Enter Fuel Usage (Litres): ")
FuelUsage = int(Feed)
Consumption = ((FuelUsage*100)/Distance)
Consumption = int(Consumption)
print(f"Fuel Consumption is {Consumption} 1 per 100km")