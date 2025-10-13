#Temp Application
print("Welcome to the app")
Temp = int(input("What is the temperature of your CPU?: "))

if Temp > 80:
    if Temp > 99:
        print("The CPU is toast. Ger your fire extinguisher")
    else:
        print("Your temp is too high")
else:
    print("Everything cool keep going")

# > greater 
# < less
# >= greater or equal 
# <= less or equal
# == equal to 
# != not equal to 

# Make a program which checks if the num is odd or even 
print("Program starting")
num = int(input("Enter a number: "))

# 1 = odd 0 = even 
Remainder = num % 2 
if Remainder == 1:
    print(f"{num} is a odd number")
elif Remainder == 0:
    print(f"{num} is an even number")
