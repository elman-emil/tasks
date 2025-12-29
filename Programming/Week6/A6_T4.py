def readfile(filename: str) -> str:
    file = open(filename, "r")
    content = ""

    row = file.readline()
    while row != "":
        if row != "\n":                     
            if row[-1] == "\n":             
                row = row[:-1]
            content += row + ";"
        row = file.readline()

    file.close()
    return content


def analyse_names(content: str):
    names = content.split(";")

    count = len(names)
    total_length = 0

    shortest = len(names[0])
    longest = len(names[0])

    for name in names:
        name_length = len(name)
        total_length = total_length + name_length

        if name_length < shortest:
            shortest = name_length

        if name_length > longest:
            longest = name_length

    average = total_length / count
    return count, shortest, longest, average


def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")

    print('Reading names from "' + filename + '".')
    content = readfile(filename)

    print("Analysing names...")
    count, shortest, longest, average = analyse_names(content)

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count --", count)
    print("Shortest name --", shortest, "chars")
    print("Longest name --", longest, "chars")
    print("Average name -- {:.2f} chars".format(average))
    print("#### REPORT END ####")
    print("Program ending.")

    return None


main()



