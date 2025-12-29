#Demo code 
import sys

print("Program starting.")
filename = input("Insert filename: ")

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("Error: File does not exist.")
    sys.exit(1)

values = ""

row = file.readline()
while row != "":
    row = row.strip()         

    if row != "":             
        if values == "":
            values = row
        else:
            values += "," + row

    row = file.readline()

file.close()

print("\nVertical output:")
parts = values.split(",")

for value in parts:
    print(value)

print("\nHorizontal output:")
horizontal = ""

for value in parts:
    if horizontal == "":
        horizontal = value
    else:
        horizontal += ", " + value

print(horizontal)

print("Program ending.")

