print("Program starting.")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print()
print("Starting for-loop: ")
if start <= stop:
    for i in range(start, stop + 1):
        print(i)
    else:
        for i in range(start, stop -1, -1):
            print(i)
print()
print("Program ending.")
    