def askpositiveInteger() -> int:
    positiveInt = -1
    Feed = input("Insert positive integer (negative stops): ")
    if Feed.isnumeric():
        positiveInt = int(Feed)
    
    return positiveInt


def displayInteger(Numbers: list[int]):
    if len(Numbers) == 0:
        print("No inetegers to display")
    else:
        print(f"Displaying {len(Numbers)} integers:")
        index = 0 
        for list in Numbers:
            ordinal = index + 1

            print(f"- Index {index} -> ordinal {ordinal} => Integer {list} ")
            index += 1
    
    return None 


def main():
    print("Program starting.")
    print("Collect positive integers.")
    positiveInt: list[int] = []
    currentInteger = askpositiveInteger()
    while currentInteger >= 0:
        
        positiveInt.append(currentInteger)
        currentInteger = askpositiveInteger()
        
    print("Stopped collecting positive inetegers.")
    displayInteger(positiveInt)
    
    return None 

if __name__ == "__main__":
    
    main()

