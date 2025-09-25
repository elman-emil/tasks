print("Program starting.")
Temp = float(input("Insert Fahrenheits: "))
Celcius = (Temp - 32) / 1.8
Celcius = round(Celcius, 1)

print(f"{Temp}°F is {Celcius}°C")

print("Program ending.")