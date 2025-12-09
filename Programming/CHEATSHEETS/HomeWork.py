# Turtle in a straight line

# import turtle
# sipi = turtle.Turtle() #creates a new object of a class
# sipi.shape("turtle") #method of the turtle class
# sipi.color("purple")
# sipi.forward(100)

# turtle_screen = turtle.Screen() #an instance (or object / olio in finnish) of the screen class
# turtle_screen.exitonclick() #method



####################################################

# # Ball bouncing program 
 
# import pygame 
# pygame.init()

# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Pygame Demo")

# x = 50
# y = 200
# speed = 0.4
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     x += speed 
#     if x > 600 or x < 0:
#         speed = -speed 

    
#     screen.fill((255, 255, 255))
#     pygame.draw.circle(screen, (0,0,255),(x,y), 20)

#     pygame.display.update()

# pygame.quit()


##############################################################

# FUNCTIONS



def my_name():
    return ("Elman Ahmed Emil")

name = my_name()
print(name)





#------------------------------------------

# def fahrenheit_to_celsius(fahrehheit):
#     return (fahrehheit - 32) * 5 / 9 

# #now

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(65))

#-------------------------------------------

# def get_greeting():
#     return "Hello sir, welcome back to the program"

# message = get_greeting()
# print(message)

# #---------------------------------------------







