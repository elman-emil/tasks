def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def main():
    print("Basic Calculator Program")
    print("All operations use floating point numbers.")

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "5":
            print("Program ended.")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            print("Invalid choice. Try again.")
            continue

        print("Result:", result)

main()
