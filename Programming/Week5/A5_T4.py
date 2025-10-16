def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth, PHeight) -> float:
   print("")
   Area = PWidth * PHeight
   return float(Area)

# Area = calculateArea()
# print("")
# print("Area is {Area}²")
# print("end")

def main() -> None: 
   print("Program starting.")
   Width = askDimension("width")
   Height = askDimension("height")
   Area = calcRectangleArea(Width, Height)
   print("")
   print(f"Area is {Area}")
   print("Program ending.")
   return None 

main()
