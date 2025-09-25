#A2_T1
print("Program starting.")
name = input("What is your name?: ")
num1 = float(input("Enter a floating point number: "))
num2 = float(input("Enter a second floating point number: "))
print(name, "you gave numbers", num1, "and", num2)
product = round(num1*num2, 2)
print("Multiplying first and second number will result in product", product)
print("Program ending.")



#A2_T2
print("Program starting.")
brand = input("Insert car brand: ")
model = input("Insert car model: ")
print("Car brand is", '"' + brand + '"', sep= " ", end= " ")
print("and the model is", "'" + model + "'.", sep= " ") 
print("Program ending.")



#A2_T3
print("Program starting.")
word1 = input("Insert first word: ")
word2 = input("Insert second word: ")
print("1st word is", len(word1), "characters long.")
print("2nd word is", len(word2), "characters long.")
compound = word1 + word2
print("Words together makes one closed compound", "'" + compound + "'.")
print("Program ending.")



#A2_T4
print("Program starting.")
print("Estimate how many minutes you spent on programming...")
t1 = int(input("A1_T1: "))
t2 = int(input("A1_T2: "))
t3 = int(input("A1_T3: "))
t4 = int(input("A1_T4: "))
t5 = int(input("A1_T5: "))
t6 = int(input("A1_T6: "))
t7 = int(input("A1_T7: "))
total = t1 + t2 + t3 + t4 + t5 + t6 + t7
average = total / 7
average_two_decimals = round(average, 2)
average_integer = round(average)
print("\nIn total you spent", total, "minutes on programming.")
print("Average per task was", average_two_decimals, "min and same rounded to the nearest integer", average_integer, "min.")
print("\nProgram ending.")




#A2_T5
print("Program starting.")
word = input("Insert a closed compound word: ")
print("The word you inserted is '" + word + "' and in reverse it is '" + word[::-1] + "'.")
print("The inserted word length is", len(word))
print("Last character is '" + word[-1] + "'")
print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = word[start:end:step]
print("\nThe word '" + word + "' sliced to the defined substring is '" + substring + "'.")
print("Program ending.")





#A2_T6
print("Program starting.")
print()

Hex = input("Insert a Hex color: ")
Hex = Hex.replace("#","").strip().upper()
print()

print("colors")
print(f"- Red {Hex[:2]}")
print(f"- Green {Hex[2:4:]}")
print(f"- Blue {Hex[4:6:]}")
print()

print("Program ending.")




#A2_T7
print("Program starting.")
fahrenheit = float(input("Insert fahrenheits: "))
celsius = (fahrenheit - 32) / 1.8

print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C")

print("Program ending.")





