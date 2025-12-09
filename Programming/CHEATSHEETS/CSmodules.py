import pandas as pd
import matplotlib.pyplot as plt 

data = {
    'temperature': [23,23,21,20,19,15,12,23,25,30],
    'movement': [1,0,1,1,1,1,0,0,1,1]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(10,5))
plt.plot(df['temperature'], label = "Temperature")
plt.plot(df['movement'], label = "Movemenet")
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Movement Over Time')
plt.legend()
plt.show()

#######################################################################################################################

import turtle
sipi = turtle.Turtle() #creates a new object of a class
sipi.shape("turtle") #method of the turtle class
sipi.color("purple")
sipi.forward(100)

turtle_screen = turtle.Screen() #an instance (or object / olio in finnish) of the screen class
turtle_screen.exitonclick() #method


#########################################################################################################################

class LABStudent:
    name = str #attribute
    age = int #attribute
    major = str #attribute

    def introduce(self): #Method, ask the object to do something
        return f"Hi, I'm {self.name}, {self.age} years, majoring in {self.major}"
    
    def study(self): #Method
        return f"{self.name} is now studying {self.major}"

John = LABStudent() #object or instance of LABstudent
John.name = "john"
John.age = 32
John.major = "Biology"

Jane = LABStudent()
Jane.name = "Jane"
Jane.age = 26 
Jane.major = "ICT"

print(John.introduce()) 
print(Jane.introduce())

###########################################################################################################################

class LABStudent:
    #Constructor method to initialize attributes 

    def __init__(self, name, age, major):
        self.name = name 
        self.age = age
        self.major = major
    
    def introduce(self): #Method, ask the object to do something
        return f"Hi, I'm {self.name}, {self.age} years, majoring in {self.major}"
    
    def study(self): #Method
        return f"{self.name} is now studying {self.major}"
    
John = LABStudent("John", 32, "Biology")
Jane = LABStudent("Jane", 26, "ICT")

print(John.introduce()) 
print(Jane.introduce())

#############################################################################################################################

from lab_student import LABStudent 

John = LABStudent("John", 32, "Biology")
Jane = LABStudent("Jane", 26, "ICT")

print(John.introduce())
print(Jane.introduce())


##############################################################################################################################




