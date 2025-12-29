def readFile(filename: str) -> list:
    file = open(filename, "r")
    timestamps = []

    row = file.readline()  # skip header
    row = file.readline()

    while row != "":
        if row[-1] == "\n":
            row = row[:-1]
        timestamps.append(row)
        row = file.readline()

    file.close()
    return timestamps


def analyseTimestamps(timestamps: list) -> list:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

    day_usage = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    day_cost = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for row in timestamps:
        parts = row.split(";")
        timestamp = parts[0]
        consumption = float(parts[1])
        price = float(parts[2])

        day_index = int(timestamp.split("-")[2].split(" ")[0]) % 7

        day_usage[day_index] += consumption
        day_cost[day_index] += consumption * price

    results = []

    for i in range(7):
        line = (
            "-- " + days[i] +
            " usage: {:.2f} kWh, cost: {:.2f} €"
            .format(day_usage[i], day_cost[i])
        )
        results.append(line)

    return results


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    print('Reading file "' + filename + '".')
    timestamps = readFile(filename)

    print("Analysing timestamps.")
    results = analyseTimestamps(timestamps)

    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for line in results:
        print(line)

    print("### Electricity consumption summary ###")
    print("Program ending.")

    return None


main()
