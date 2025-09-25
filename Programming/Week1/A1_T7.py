#Task7
print("Calculate fuel consumption.")
Feed = input("Enter Travel Distance (Kilometers): ")
Distance = int(Feed)
Feed = input("Enter Fuel Usage (Litres): ")
FuelUsage = int(Feed)
Consumption = ((FuelUsage*100)/Distance)
Consumption = int(Consumption)
print(f"Fuel Consumption is {Consumption} 1 per 100km")