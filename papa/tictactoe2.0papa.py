import turtle

tina = turtle.Turtle()
tina.shape("circle")
tina.pensize(3)
tina.speed(100000000000000)

# number of squares in a row/column.
m = 3

# size of small square
z = 100


def draw_square(x, y):
    tina.penup()
    tina.goto(x, y)
    tina.pendown()
    for i in range(4):
        tina.forward(z)
        tina.right(90)


def draw_column(x):
    for i in range(m):
        draw_square(x * z, i * z)


def draw_big_square():
    for i in range(m):
        draw_column(i)


draw_big_square()

tina.hideturtle()

turtle.done()
