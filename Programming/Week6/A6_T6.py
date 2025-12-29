def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:

            result += char

    return result


def main():
    print("Multi-line Caesar Cipher")

    
    lines = []
    while True:
        row = input()
        if row == "":
            break
        lines.append(row)

    if len(lines) == 0:
        print("No input provided.")
        return

    shift = int(input("Enter shift value: "))

    
    ciphered_lines = [caesar_cipher(line, shift) for line in lines]

    
    choice = input("Choose: ""s"" to show cipher or ""w"" to write te to file ? ").lower()

    if choice == "s":
        print("\nCiphered text:")
        for line in ciphered_lines:
            print(line)

    elif choice == "w":
        filename = input("Enter filename to save: ")
        with open(filename, "w") as f:
            for line in ciphered_lines:
                f.write(line + "\n")
        print("Cipher saved to", filename)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
