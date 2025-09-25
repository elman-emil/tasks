#A2_T5
print("Program starting.")
word = input("Insert a closed compound word: ")
print("The word you inserted is '" + word + "' and in reverse it is '" + word[::-1] + "'.")
print("The inserted word length is", len(word))
print("Last character is '" + word[-1] + "'")
print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = word[start:end:step]
print("\nThe word '" + word + "' sliced to the defined substring is '" + substring + "'.")
print("Program ending.")

