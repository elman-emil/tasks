# Logic taken from copilot
import sys

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Recursive Factorial Calculator")

user_input = input("Insert a non-negative integer: ")

try:
    number = int(user_input)
except ValueError:
    print("Error: Input must be an integer.")
    sys.exit(1)

if number < 0:
    print("Error: Factorial is not defined for negative numbers.")
    sys.exit(1)

result = factorial(number)

print("Factorial of {} is {}".format(number, result))
