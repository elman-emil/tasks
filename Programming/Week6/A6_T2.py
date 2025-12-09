def main()-> None:
    print("Program starting.")
    firstnam = input("Insert first name: ")
    lastnam = input("Insert last name: ")
    filename = input("Insert filename: ")
    


    file = open(filename, 'w')
    file.write(firstnam + '\n' )
    file.write(lastnam + '\n')
    file.close
    return None



main()




