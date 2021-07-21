import turtle
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
        tina.write(
            i,
            align="center",
            font=("Comic Sans MS", int(round(radius / 12.5, 0)), "normal"),
        )
        tina.penup()
        tina.forward(14)
        tina.right(i * 30)
        tina.backward(radius * 0.75)


def find_time():
    now = datetime.datetime.now()
    clock_string = now.strftime("%Y-%m-%d %H:%M:%S")
    date, time = clock_string.split(" ")
    hours, minutes, seconds = time.split(":")
    return int(hours), int(minutes), int(seconds)


def make_hand(angle, length, color):
    tina.pendown()
    tina.right(angle)
    tina.pencolor(color)
    tina.forward(length)
    tina.backward(length)
    tina.left(angle)
    tina.penup()


def make_erase_hand(angle, e_angle, length, color, e_color):
    make_hand(e_angle, length, e_color)
    make_hand(angle, length, color)


make_clock(radius)
hours, minutes, seconds = find_time()

seconds_old = seconds
minutes_old = minutes
sec_hand_len = radius / 3 * 2
min_hand_len = radius / 2 + (radius / 10)
hour_hand_len = radius / 2
sec_color = "red"
min_color = "black"
hour_color = "black"
erase_color = "white"
second_angle = 360 / 60 * seconds
minute_angle = 360 / 60 * minutes
hour_angle = 360 / 12 * hours + (minute_angle / 6)
sec_erase_angle = second_angle - 6
min_erase_angle = minute_angle - 6
hour_erase_angle = hour_angle - 1.5
make_hand(minute_angle, min_hand_len, min_color)
make_hand(hour_angle, hour_hand_len, hour_color)


is_clock_active = True
while is_clock_active:
    hours, minutes, seconds = find_time()
    if hours > 12:
        hours -= 12
    second_angle = 360 / 60 * seconds
    minute_angle = 360 / 60 * minutes
    hour_angle = 360 / 12 * hours + (minute_angle / 6)
    if seconds == 0:
        seconds_old = 0
        make_erase_hand(
            second_angle, sec_erase_angle, sec_hand_len, sec_color, erase_color
        )
        sec_erase_angle = second_angle
    if seconds_old != seconds:
        make_erase_hand(
            second_angle, sec_erase_angle, sec_hand_len, sec_color, erase_color
        )
        seconds_old = seconds
        sec_erase_angle = second_angle
        print("secs:", seconds_old)
    if minutes == 0:
        minutes_old = 0
        make_erase_hand(
            minute_angle, min_erase_angle, min_hand_len, min_color, erase_color
        )
        make_erase_hand(
            hour_angle, hour_erase_angle, hour_hand_len, hour_color, erase_color
        )
        min_erase_angle = minute_angle
    if minutes_old != minutes:
        make_erase_hand(
            minute_angle, min_erase_angle, min_hand_len, min_color, erase_color
        )
        make_erase_hand(
            hour_angle, hour_erase_angle, hour_hand_len, hour_color, erase_color
        )
        minutes_old = minutes
        min_erase_angle = minute_angle
        hour_erase_angle = hour_angle
        print("minutes:", minutes_old, "hours:", hours)
    if minute_angle + 10 > second_angle > minute_angle - 10:
        make_hand(minute_angle, min_hand_len, min_color)
    if hour_angle + 30 > second_angle > hour_angle - 30:
        make_erase_hand(
            hour_angle, hour_erase_angle, hour_hand_len, hour_color, erase_color
        )
        hour_erase_angle = hour_angle
    if hour_angle + 6.75 > minute_angle > hour_angle - 6.75:
        make_erase_hand(
            hour_angle, hour_erase_angle, hour_hand_len, hour_color, erase_color
        )
        hour_erase_angle = hour_angle
