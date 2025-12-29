SEPARATOR = ";"

def readValues(filename: str) -> str:
    file = open(filename, "r")
    values = ""

    row = file.readline()
    while row != "":
        if row[-1] == "\n":          
            row = row[:-1]
        values += row + SEPARATOR
        row = file.readline()

    file.close()
    return values


def analyseNumbers(values: str):
    numbers = values.split(SEPARATOR)

    count = len(numbers)
    total = 0
    greatest = int(numbers[0])

    for number in numbers:
        value = int(number)
        total = total + value

        if value > greatest:
            greatest = value

    average = total / count
    return count, total, greatest, average


def main() -> None:
    print("Program starting.")

    filename = input("Insert filename: ")

    values = readValues(filename)

    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    print("Count;Sum;Greatest;Average")

    count, total, greatest, average = analyseNumbers(values)

    print(
        str(count) + ";" +
        str(total) + ";" +
        str(greatest) + ";" +
        "{:.2f}".format(average)
    )

    print("\n#### Number analysis - END ####")
    print("Program ending.")

    return None


main()
