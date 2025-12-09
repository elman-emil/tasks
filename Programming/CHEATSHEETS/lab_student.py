# JUST A FILE FOR IMPORT PURPOSES (NOT A CODE.)

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

