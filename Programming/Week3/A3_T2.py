print("Program starting.")
print("String comparisons")
word1 = input("Insert first word: ")

character = input("Insert a character: ")
if(character in word1):
    print(f"word \"{word1}\" contains character \"{character}\"") 
else:
    print(f"word \"{word1}\" doesnt contain character \"{character}\"")

word2 = input("Insert second word: ")
if (word2 > word1):
    print(f"The first word \"{word1}\" is before the second word \"{word2}\" alphabetically") 
elif (word1 > word2):
    print(f"The second word \"{word2}\" is before the first word \"{word1}\" alphabetically")

print("Program ending.")
