#A2_T6
print("Program starting.")
print()

Hex = input("Insert a Hex color: ")
Hex = Hex.replace("#","").strip().upper()
print()

print("colors")
print(f"- Red {Hex[:2]}")
print(f"- Green {Hex[2:4:]}")
print(f"- Blue {Hex[4:6:]}")
print()

print("Program ending.")
