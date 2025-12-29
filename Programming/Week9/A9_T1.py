total_sum = 0.0

while True:
    user_input = input("Insert a floating-point value (0 to stop): ")

    try:
        value = float(user_input)
    except ValueError:
        print("Error: '{}' couldn't be converted to a floating-point number.".format(user_input))
        continue

    if value == 0:
        break

    print("You entered: {}".format(value))
    total_sum += value

print("Sum of inserted values: {:.2f}".format(total_sum))
