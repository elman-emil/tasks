def main()-> None:
    print("Program starting.")
    print("This program can read a file")
    filename = input("Insert the file name: ")
    print(f"### START '{filename}' ####")
    file = open(filename, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break 
        print(line, end='')
    file.close()
    print()
    print(f"#### END '{filename}' ####")

    print("Program ending.")



main()




