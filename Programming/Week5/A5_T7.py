def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return words

def analyseWords(words):
    if not words:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return
    count = len(words)
    total = sum(len(w) for w in words)
    avg = total / count
    print(f"- {count} Words")
    print(f"- {total} Characters")
    print("- {:.2f} Average word length".format(avg))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()