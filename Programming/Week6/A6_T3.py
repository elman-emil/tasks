def readfile(filename: str) -> str:
    file = open(filename, "r")
    content = ""
    Row = file.readline()
    while Row != "":
        content += Row 
        Row = file.readline()
        if len(Row) == 0:
            break
        file.close() 
    return content 

def writefile(filecontent, Dfilename):
    file = open(Dfilename, "w")
    file.write(filecontent)
    file.close 

def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")
    filename = input("Insert Source file name: ")
    Dfilename = input("Insert Destination file name: ")
    filecontent = readfile(filename)
    writefile(filecontent, Dfilename)
    
    print("Program ended.")
    return None 

main()

