import turtle

x = 50

# turtles
tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(20)
tina.left(90)
tina.penup()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.pensize(3)
tommy.speed(20)
tommy.left(90)
tommy.penup()

tommy.goto(x / 2, x)
tina.goto(-x / 2, x)


def move_both(dis):
    tina.forward(dis)
    tommy.forward(dis)


def turn_both():
    tommy.right(90)
    tina.left(90)


def both():
    move_both(x * 3)
    turn_both()


def both_turn():
    tommy.left(90)
    tina.right(90)


turn_both()
tina.pendown()
tommy.pendown()
move_both(x)
turn_both()

for i in range(4):
    both()

turn_both()
move_both(x)

dist = [3, 1, 2, 3, 1, 3]
for d in dist:
    both_turn()
    move_both(d * x)

tina.hideturtle()
tommy.hideturtle()
turtle.done()
