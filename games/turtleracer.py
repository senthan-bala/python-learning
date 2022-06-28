import turtle
from random import randint


def create_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(3)
    t.speed(100)
    return t


nila = turtle.Turtle()
nila.shape("turtle")
nila.pensize(3)
nila.color("red")

sanvi = turtle.Turtle()
sanvi.shape("turtle")
sanvi.pensize(3)
sanvi.color("blue")

juhi = turtle.Turtle()
juhi.shape("turtle")
juhi.pensize(3)
juhi.color("green")


# 16 is the max with 30 spacing
no_of_turtles = 5
spacing = 30
min_x_pos = 0


def make_single_track(racer, i, x, number):
    racer.goto(x, 0)
    racer.pendown()
    racer.forward(300)
    racer.penup()
    racer.forward(20)
    racer.write(number)


def make_full_track():
    global min_x_pos
    for i in range(no_of_turtles):
        tt = create_turtle()
        tt.left(90)
        tt.penup()
        x1 = i * (-spacing)
        make_single_track(tt, i, x1, i + 1)
        x2 = i * (-spacing) - (no_of_turtles * spacing)
        min_x_pos = x2
        make_single_track(tt, i, x2, i + 1 + no_of_turtles)
        tt.hideturtle()


nila_step_size = randint(35, 45)
sanvi_step_size = randint(35, 45)
juhi_step_size = randint(35, 45)


def get_start_pos():
    return min_x_pos - 15


def ready_up():
    nila.penup()
    nila.goto(get_start_pos(), 50)
    nila.pendown()
    sanvi.penup()
    sanvi.goto(get_start_pos(), 150)
    sanvi.pendown()
    juhi.penup()
    juhi.goto(get_start_pos(), 250)
    juhi.pendown()
    juhi.penup()
    nila.penup()
    sanvi.penup()
    juhi.circle(20)
    sanvi.circle(20)
    nila.circle(20)
    juhi.pendown()
    nila.pendown()
    sanvi.pendown()


def is_race_still_on(nila_x_pos, sanvi_x_pos, juhi_x_pos):
    is_nila_not_done = nila_x_pos < 0
    is_sanvi_not_done = sanvi_x_pos < 0
    is_juhi_not_done = juhi_x_pos < 0
    return is_nila_not_done and is_sanvi_not_done and is_juhi_not_done


def find_winner(nila_x_pos, sanvi_x_pos, juhi_x_pos):
    spaces = " " * 10
    if nila_x_pos >= 0 and sanvi_x_pos >= 0 and juhi_x_pos >= 0:
        nila.write(spaces + "It is a tie!!!")
        sanvi.write(spaces + "It is a tie!!!")
        juhi.write(spaces + "It is a tie!!!")
    elif nila_x_pos >= 0 and juhi_x_pos >= 0:
        nila.write(spaces + "It is a tie!")
        juhi.write(spaces + "It is a tie!")
    elif nila_x_pos >= 0 and sanvi_x_pos >= 0:
        nila.write(spaces + "It is a tie!")
        sanvi.write(spaces + "It is a tie!")
    elif juhi_x_pos >= 0 and sanvi_x_pos >= 0:
        sanvi.write(spaces + "It is a tie!")
        juhi.write(spaces + "It is a tie!")
    elif nila_x_pos >= 0:
        nila.write(spaces + "I win!")
    elif juhi_x_pos >= 0:
        juhi.write(spaces + "I win!")
    else:
        sanvi.write(spaces + "I win!")


def start_racing():
    nila_x_pos = get_start_pos()
    sanvi_x_pos = get_start_pos()
    juhi_x_pos = get_start_pos()
    while is_race_still_on(nila_x_pos, sanvi_x_pos, juhi_x_pos):
        nila.forward(nila_step_size)
        nila_x_pos = nila_x_pos + nila_step_size
        sanvi.forward(sanvi_step_size)
        sanvi_x_pos = sanvi_x_pos + sanvi_step_size
        juhi.forward(juhi_step_size)
        juhi_x_pos = juhi_x_pos + juhi_step_size
    find_winner(nila_x_pos, sanvi_x_pos, juhi_x_pos)


make_full_track()
ready_up()
start_racing()

turtle.done()
