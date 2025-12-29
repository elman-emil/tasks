import sys

filename = input("Insert CSV filename: ")

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("Error: File does not exist.")
    sys.exit(1)

print("Timestamps found in file:")

row = file.readline()
while row != "":
    # Split the row using semicolon separator
    parts = row.split(";")

    # Timestamp is the first value
    timestamp = parts[0]

    print(timestamp)

    row = file.readline()

file.close()

print("Program finished normally.")
