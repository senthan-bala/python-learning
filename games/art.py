import turtle
import pygame
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


def make_triangle(tp):
    t1 = randint(45, 100)
    t2 = randint(45, 180 - t1)
    t3 = 180 - (t1 + t2)
    tina.forward(randint(30, 80))
    tina.left(t1)
    tina.forward(randint(30, 80))
    tina.left(t2)
    tina.goto(tp)


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
for i in range(randint(75, 200)):
    s_length = randint(10, 50)
    l_length = randint(30, 100)
    tina.color(choice(colors))
    tina.left(randint(10, 100))
    tina.penup()
    tina.goto(randint(-400, 400), randint(-400, 400))
    tina.pendown()
    make_full_rect(s_length, l_length)
for i in range(randint(75, 200)):
    tina.penup()
    tina.goto(randint(-400, 400), randint(-400, 400))
    tina.pendown()
    tina.begin_fill()
    tina.color(choice(colors))
    tina.circle(randint(10, 30))
    tina.end_fill()
for i in range(randint(75, 200)):
    t_place = randint(-400, 400), randint(-400, 400)
    tina.penup()
    tina.goto(t_place)
    tina.pendown()
    tina.begin_fill()
    tina.color(choice(colors))
    make_triangle(t_place)
    tina.end_fill()


tina.hideturtle()
turtle.done()
