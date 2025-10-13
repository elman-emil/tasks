print("Program starting.\n")
starting = int(input("Insert starting point: "))
stopping = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
print()
valid = True
if starting >= stopping:
    print("Starting point value must be less than the stopping point value.")
    valid = False
if inspection < starting or inspection > stopping:
    print("Inspection value must be within the range of start and stop.")
    valid = False
if valid:
    print("First loop - inspection with break:")
    for i in range(starting, stopping):
        if i >= inspection:
            break
        if i != starting:
            print(" ", end="")
        print(i, end="")
    print("\nSecond loop - inspection with continue:")
    first = True
    for i in range(starting, stopping):
        if i == inspection:
            continue
        if not first:
            print(" ", end="")
        print(i, end="")
        first = False
print("\n\nProgram ending.")