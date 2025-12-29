import sys

def read_timestamps(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
        sys.exit(1)

    data = ""
    row = file.readline()
    while row != "":
        data += row
        row = file.readline()

    file.close()
    return data


def count_by_year(data, year):
    count = 0
    lines = data.split("\n")

    for line in lines:
        if line != "" and line[0:4] == year:
            count += 1

    return count


def count_by_month(data, month):
    count = 0
    lines = data.split("\n")

    for line in lines:
        if line != "" and line[5:7] == month:
            count += 1

    return count


def count_by_weekday(data, weekday):
    count = 0
    lines = data.split("\n")

    for line in lines:
        if weekday.lower() in line.lower():
            count += 1

    return count


def main():
    print("Program starting.")

    data1 = read_timestamps("A8_T1D1.txt")
    data2 = read_timestamps("A8_T1D2.txt")

    all_data = data1 + data2

    while True:
        print("\nMenu:")
        print("1 - Count by year")
        print("2 - Count by month")
        print("3 - Count by weekday")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            year = input("Insert year (YYYY): ")
            result = count_by_year(all_data, year)
            print("Timestamps in year", year, ":", result)

        elif choice == "2":
            month = input("Insert month (MM): ")
            result = count_by_month(all_data, month)
            print("Timestamps in month", month, ":", result)

        elif choice == "3":
            weekday = input("Insert weekday (e.g. Monday): ")
            result = count_by_weekday(all_data, weekday)
            print("Timestamps on", weekday, ":", result)

        elif choice == "0":
            print("Program ending.")
            break

        else:
            print("Invalid choice.")

main()
