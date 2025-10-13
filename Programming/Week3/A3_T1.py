print("Program starting.")

print("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))

if num1 == num2:
    print("Integers are the same")
if num1 > num2:
    print(f"Integer {num1} is greater than {num2}")
if num1 < num2:
    print(f"Integer {num2} is greater than {num1}")
print()
print("Adding integers together")
print(f"{num1} + {num2} = {(num1 + num2)}")
print()
print("Checking the parity of the sum")
sum = num1 + num2 
Remainder = sum % 2
if Remainder == 1:
    print("Sum is even")
elif Remainder == 0:
    print("Sum is odd")


print("Program ending.")





