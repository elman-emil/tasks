import sys
print("Program starting.")
filename = input("Insert filename: ")

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("Couldnt read file 'non-existing.txt'")
    sys.exit(1)

content = file.read()
file.close()

print("File content:")
print(content)

print("Program continues normally.")