import sys

def readfile(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Error: Source file does not exist.")
        sys.exit(1)

    content = ""
    row = file.readline()
    while row != "":
        content += row
        row = file.readline()

    file.close()
    return content


def writefile(content, filename):
    try:
        file = open(filename, "w")
    except IOError:
        print("Error: Could not write destination file.")
        sys.exit(1)

    file.write(content)
    file.close()


def main():
    if len(sys.argv) != 3:
        print("Usage: python copyfile.py <source_file> <destination_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    print("Program starting.")
    print("Copying file:", source_file, "->", destination_file)

    content = readfile(source_file)
    writefile(content, destination_file)

    print("File copied successfully.")
    print("Program ending.")


main()

