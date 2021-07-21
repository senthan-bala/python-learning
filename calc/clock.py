import turtle
import time
import datetime

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(100)
tina.hideturtle()

radius = 200


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
        tina.write(i, align="center", font=("Comic Sans MS", 16, "normal"))
        tina.penup()
        tina.forward(14)
        tina.right(i * 30)
        tina.backward(radius * 0.75)


make_clock(radius)


def make_hand(pen, color, angle, size):
    clockline.pensize(pen)
    clockline.pencolor(color)
    clockline.right(angle)
    clockline.forward(size)
    clockline.backward(size)
    clockline.left(angle)


def del_hand(pen, del_color, angle, size):
    clockline.pensize(pen)
    clockline.right(angle - 6)
    clockline.pencolor(del_color)
    clockline.forward(size)
    clockline.backward(size)
    clockline.left(angle - 6)


def backup_hand(
    check, main1, main2, mpen, mcolor, mangle, msize, hpen, hcolor, hangle, hsize
):
    if main1 - 60 < check < main1 + 60:
        make_hand(hpen, hcolor, hangle, hsize)
    if main2 - 60 < check < main2 + 60:
        make_hand(mpen, mcolor, mangle, msize)


clockline = turtle.Turtle()
clockline.hideturtle()
clockline.speed(100)
clockline.pensize(2)

clockline.left(90)

second_color = "red"
minute_color = "black"
hour_color = "black"
del_color = "white"
second_size = 120
minute_size = 95
hour_size = 70
second_pen = 2
minute_pen = second_pen * 3
hour_pen = second_pen * 3

now = datetime.datetime.now()
clock_string = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time : ", clock_string)
clock_list1 = clock_string.split(" ")
clock_list2 = (clock_list1[1]).split(":")
minute_angle = (int(clock_list2[1]) / 60) * 360
if int(clock_list2[0]) > 12:
    hour_angle = ((int(clock_list2[0]) - 12) / 12) * 360 + (minute_angle / 12)
elif int(clock_list2[0]) <= 12:
    hour_angle = (int(clock_list2[0]) / 12) * 360 + (minute_angle / 12)
second_angle = (int(clock_list2[2]) / 60) * 360

make_hand(minute_pen, minute_color, minute_angle, minute_size)
make_hand(hour_pen, hour_color, hour_angle, hour_size)


minutes = 0
seconds_old = clock_list2[2]
seconds = int(seconds_old)


Exit = False
while Exit == False:
    seconds_old = clock_list2[2]
    minutes_old = clock_list2[1]
    hours_old = clock_list2[0]
    now = datetime.datetime.now()
    clock_string = now.strftime("%Y-%m-%d %H:%M:%S")
    clock_list1 = clock_string.split(" ")
    clock_list2 = (clock_list1[1]).split(":")
    minute_angle = (int(clock_list2[1]) / 60) * 360
    if int(clock_list2[0]) > 12:
        hour_angle = ((int(clock_list2[0]) - 12) / 12) * 360 + (minute_angle / 12)
    elif int(clock_list2[0]) < 12:
        hour_angle = (int(clock_list2[0]) / 12) * 360 + (minute_angle / 12)
    second_angle = (int(clock_list2[2]) / 60) * 360
    if (
        int(clock_list2[2]) > int(seconds_old)
        or int(clock_list2[2]) == 0
        and int(seconds_old) == 59
    ):
        seconds = seconds + 1
        # Adds new second hand
        make_hand(second_pen, second_color, second_angle, second_size)
        # Removes original second hand
        del_hand(second_pen, del_color, second_angle, second_size)
        backup_hand(
            second_angle,
            hour_angle,
            minute_angle,
            minute_pen,
            minute_color,
            minute_angle,
            minute_size,
            hour_pen,
            hour_color,
            hour_angle,
            hour_size,
        )
    # while seconds < 60:
    if (
        int(clock_list2[1]) > int(minutes_old)
        or int(clock_list2[1]) == 0
        and int(minutes_old) == 59
    ):
        # Removes original minute hand
        del_hand(minute_pen, del_color, minute_angle, minute_size)
        # Adds new minute hand
        make_hand(minute_pen, minute_color, minute_angle, minute_size)
        backup_hand(
            minute_angle,
            second_angle,
            hour_angle,
            minute_pen,
            minute_color,
            minute_angle,
            minute_size,
            hour_pen,
            hour_color,
            hour_angle,
            hour_size,
        )
        # Removes original hour hand
        del_hand(hour_pen, del_color, hour_angle, hour_size)
        # Adds new hour hand
        make_hand(hour_pen, hour_color, hour_angle, hour_size)
        backup_hand(
            hour_angle,
            minute_angle,
            second_angle,
            minute_pen,
            minute_color,
            minute_angle,
            minute_size,
            hour_pen,
            hour_color,
            hour_angle,
            hour_size,
        )
