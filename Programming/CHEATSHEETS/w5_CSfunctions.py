#FUNCTIONS 


def say_hello():
    print("Hello there!")
    print("This message comes from inside the function.")
    return None 
say_hello()
print("Function executed.")


print("hello")
# print is an example of function
# hello in this case is an example of a parameter 


len("hello")
# another example of a function


def greet(name): 
    return f"Hello {name}" # return something from a function

Message = greet("Mira")
print(Message)

Message = greet("Emil")
print(Message)

def greeting(): # defining a function
    print("how do you do?") # function content

greeting() # call the function/ function call
greeting()
greeting()


def greeting_airport(person, age):
    print(f"Person: {person}, Age: {age}")

greeting_airport("Mira", 48)


def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Wlcome to your flight")
    else:
        print(f"you need to wait for {18-age} years to fly on your own.")



greeting_airport(age= 5, person= "mira")



# Q. Create a program which asks the user for a number. Then check with a function if the number is a prime number. Also, ask the user if they want to test another number as many times as they want. Tip: use function, conditionals and loops..
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5)+ 1):
        if num % i == 0:
            return False
    return True 

print("Program starting.")
print()
while True:
    number = int(input("Insert a number to test: "))
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

    again = input("Do you want to test another number? put yes or no: ")
    if again != "yes":
        print()
        print("Program ending.")
        break 
    