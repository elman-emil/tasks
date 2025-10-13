Children = 3
Hometown = "Lahti"

TownsInFinland = ["lahti", "helsinki", "lappeenranta", "oulu", "tampere"]

RandomInformation = ["mira", 48, Children, Hometown, True]

print(TownsInFinland [0])
print(TownsInFinland [-1])
print(TownsInFinland)

TownsInFinland.append("Rovanien")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland)
print(NumOfTowns)

print(TownsInFinland[NumOfTowns-1])
print(TownsInFinland[0])
print(TownsInFinland[1])
print(TownsInFinland[-1])
num = 3
print(TownsInFinland[num])
Name = len("Mira") #4
print(TownsInFinland[Name])
Greeting = len("Hi") #2
print(TownsInFinland[Greeting])

Num1 = 4
print(TownsInFinland[Num1])

Villages = ["asikkala", "hollola", "karvia", "kempele"]
Towns = ["lahti", "helsinki", "lappeenranta", "oulu", "tampere"]

VillagesAndTowns = [Villages, Towns]
print(VillagesAndTowns[1][-2])

Towns.sort()
print(Towns)

#dictionary

Teacher = {
    'name': 'juha',
    'age': 50,
    'city': 'Lahti'
}

print(Teacher['name'])
print(Teacher['city'])

Empty = {}
Empty['street'] = 'Mukkulankatu 19'

Empty = {}

Teacher['city'] = 'Tampere'

for key in Teacher:
    print(key)
    print(Teacher[key])

TownsAgain = ["lahti", "helsinki", "lappeenranta", "oulu", "tampere"]
for town in TownsAgain:
    print(f"The town of {town}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end= '')
print("")

for i in range(1, 10, 3):
    print(i)

Total = 0 
for i in range(1, 101):
    Total += i 
    print(Total)
print(Total)

#For loop
#While loop