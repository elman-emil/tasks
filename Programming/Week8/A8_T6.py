import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def draw_triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

def draw_circle():
    t.circle(50)

print("Shape drawing program started.")

while True:
    shape = input("Insert shape (square / triangle / circle / exit): ")

    if shape == "square":
        draw_square()

    elif shape == "triangle":
        draw_triangle()

    elif shape == "circle":
        draw_circle()

    elif shape == "exit":
        print("Program ending.")
        break

    else:
        print("Unknown shape.")

screen.mainloop()
