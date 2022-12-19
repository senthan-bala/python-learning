import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(100)
tina.hideturtle()
radius = 200

h_color = "red"
m_color = "grey"
erase_color = "white"

m_length = radius / 2 + (radius / 10)
h_length = (radius / 5) * 2
timeExists = False


def take_time():
    time = input("What time would you like?:")

    if timeExists:
        erase_hand(h_angle, m_angle)

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minute_angle = minutes * 6
    if hours >= 12:
        hours = hours % 12
    if minutes >= 60:
        minutes = minutes % 60
    hour_angle = hours * 30
    hour_angle = hour_angle + (minutes * 0.5)
    return hour_angle, minute_angle


def make_clock(radius):
    tina.penup()
    tina.right(90)
    tina.forward(radius)
    tina.left(90)
    tina.pendown()
    tina.circle(radius)
    tina.penup()
    tina.goto(0, 0)
    tina.left(90)
    for i in range(1, 13):
        tina.right(30)
        tina.forward(radius)
        tina.pendown()
        tina.backward(radius / 5)
        tina.penup()
        tina.backward(radius / 20)
        tina.left(i * 30)
        tina.backward(14)
        tina.pendown()
        tina.write(
            i,
            align="center",
            font=("Comic Sans MS", int(round(radius / 12.5, 0)), "normal"),
        )
        tina.penup()
        tina.forward(14)
        tina.right(i * 30)
        tina.backward(radius * 0.75)


def make_hand(angle, length, color):
    tina.pendown()
    tina.right(angle)
    tina.pencolor(color)
    tina.forward(length)
    tina.backward(length)
    tina.left(angle)
    tina.penup()


def put_hands(h_angle, m_angle):
    global timeExists
    timeExists = True
    make_hand(h_angle, h_length, h_color)
    make_hand(m_angle, m_length, m_color)


def erase_hand(h_angle, m_angle):
    global timeExists
    make_hand(h_angle, h_length, erase_color)
    make_hand(m_angle, m_length, erase_color)
    timeExists = False


make_clock(radius)
for i in range(10):
    h_angle, m_angle = take_time()
    print(h_angle, m_angle)
    put_hands(h_angle, m_angle)


turtle.done()
