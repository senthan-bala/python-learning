import turtle
from random import randint
from random import choice

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(20)
tina.left(90)


def make_half_rect(s_length, l_length):
    tina.begin_fill()
    tina.forward(s_length)
    tina.left(90)
    tina.forward(l_length)
    tina.end_fill()


def make_full_rect(s_length, l_length):
    make_half_rect(s_length, l_length)
    tina.left(90)
    make_half_rect(s_length, l_length)


colors = [
    "blue",
    "red",
    "green",
    "lime",
    "purple",
    "orange",
    "deep pink",
    "cyan",
    "yellow",
    "deep sky blue",
    "magenta",
]
for i in range(randint(200, 500)):
    s_length = randint(10, 50)
    l_length = randint(30, 100)
    tina.color(choice(colors))
    tina.left(randint(10, 100))
    tina.penup()
    tina.goto(randint(-300, 300), randint(-300, 300))
    tina.pendown()
    make_full_rect(s_length, l_length)
tina.hideturtle()
turtle.done()
