import turtle
import random

length = 100
tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(50)
tina.hideturtle()


def setup(length):
    tina.penup()
    for i in range(2):
        tina.left(90)
        tina.forward(length * 1.5)
    tina.right(180)


def make_square(length):
    tina.pendown()
    for i in range(4):
        tina.forward(length)
        tina.right(90)
    tina.forward(length)


def make_board(length):
    for i in range(4):
        for i in range(3):
            make_square(length)
        tina.right(90)


def ask_coords():
    is_x_y_wrong = True
    while is_x_y_wrong:
        x_and_y = input("Please give some coords: ")
        x, y = x_and_y.split(",")
        if x.isalpha() == True:
            x = x.upper()
            if x == "A" or x == "B" or x == "C":
                if y == "1" or y == "2" or y == "3":
                    y = y.strip()
                    is_x_y_wrong = False
                    return x, y
                else:
                    print("Try Again y is not valid")
            else:
                print("Try Again, x is not valid")
        else:
            print("Try Again, x is not valid")


def calc_xy_pos(length, x, y):
    if x == "A" and y == "1":
        xpos = -length
        ypos = length
    elif x == "A" and y == "2":
        xpos = -length
        ypos = 0
    elif x == "A" and y == "3":
        xpos = -length
        ypos = -length
    elif x == "B" and y == "1":
        xpos = 0
        ypos = length
    elif x == "B" and y == "2":
        xpos = 0
        ypos = 0
    elif x == "B" and y == "3":
        xpos = 0
        ypos = -length
    elif x == "C" and y == "1":
        xpos = length
        ypos = length
    elif x == "C" and y == "2":
        xpos = length
        ypos = 0
    elif x == "C" and y == "3":
        xpos = length
        ypos = -length
    return xpos, ypos


def make_circle(length, xpos, ypos):
    tina.penup()
    tina.goto(xpos, ypos)
    tina.pendown()
    tina.right(90)
    tina.forward((length / 2) * 0.75)
    tina.left(90)
    tina.begin_fill()
    tina.circle(length / 2.85714285714)
    tina.end_fill()
    tina.penup()


def make_x(length, xpos, ypos):
    tina.penup()
    tina.goto(xpos, ypos)
    tina.left(45)
    tina.pendown()
    for i in range(4):
        tina.forward(length / 2)
        tina.right(180)
        tina.forward(length / 2)
        tina.right(270)
    tina.penup()
    tina.right(45)


def claim_pos(counter, counters):
    is_xy_val = True
    for counter_copy in counters:
        if counter == counter_copy:
            is_xy_val = False
    return is_xy_val


def check_if_win(p, i, num2, length):
    win_write_place = -(length * 0.33), length * 2
    is_program_done = False
    if num2 == i:
        if "A,1" in p and "A,2" in p and "A,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "A,1" in p and "B,1" in p and "C,1" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "A,1" in p and "B,2" in p and "C,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "C,1" in p and "B,2" in p and "A,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "C,1" in p and "C,2" in p and "C,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "C,3" in p and "B,3" in p and "A,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "B,1" in p and "B,2" in p and "B,3" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
        elif "A,2" in p and "B,2" in p and "C,2" in p:
            print("Player 1 Won!")
            tina.goto(win_write_place)
            tina.write("Player 1 Won!")
            is_program_done = True
    else:
        if "A,1" in p and "A,2" in p and "A,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "A,1" in p and "B,1" in p and "C,1" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "A,1" in p and "B,2" in p and "C,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "C,1" in p and "B,2" in p and "A,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "C,1" in p and "C,2" in p and "C,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "C,3" in p and "B,3" in p and "A,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "B,1" in p and "B,2" in p and "B,3" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
        elif "A,2" in p and "B,2" in p and "C,2" in p:
            print("Player 2 Won!")
            tina.goto(win_write_place)
            tina.write("Player 2 Won!")
            is_program_done = True
    return is_program_done


def ask_for_window_instruct():
    is_factor_valid = False
    while not is_factor_valid:
        close_window_factor = input("Would you like to close the window?: ")
        if close_window_factor.isalpha() == True:
            close_window_factor = close_window_factor.capitalize()
            if close_window_factor == "Yes":
                turtle.Screen().bye()
                is_factor_valid = True
            elif close_window_factor == "No":
                turtle.done()
            else:
                print(close_window_factor, " is not a 'yes' or a 'no', try again")


# def check_if_win2(p, i, num2):
#     a=p[len(p)-1]
#     x,y=a.split(',')
#     if x='A':
#         x='1'
#     if x='B':
#         x='2'
#     if x='C':
#         x='3'
#     xy=x+y
#     if num2 == i:


counters = []
p1_counter = []
p2_counter = []
setup(length)
make_board(length)
for i in range(9):
    is_xy_val = False
    half_num = i / 2
    half_num2 = int(half_num)
    num2 = half_num2 * 2
    while not is_xy_val:
        counter = {}
        x, y = ask_coords()
        xpos, ypos = calc_xy_pos(length, x, y)
        counter["x"] = xpos
        counter["y"] = ypos
        x_and_comma = str(x) + ","
        xy = x_and_comma + str(y)
        is_xy_val = claim_pos(counter, counters)
        if is_xy_val == True:
            counters.append(counter)
            if num2 == i:
                p1_counter.append(xy)
                is_program_done = check_if_win(p1_counter, i, num2, length)
            else:
                p2_counter.append(xy)
                is_program_done = check_if_win(p2_counter, i, num2, length)
        else:
            print("Try again, that spot is taken")
    if num2 == i:
        make_x(length, xpos, ypos)
    elif num2 != i:
        make_circle(length, xpos, ypos)
    if is_program_done == True:
        break
    if i == 8:
        print("DRAW!")
        win_write_place = -(length * 0.20), length * 2
        tina.goto(win_write_place)
        tina.write("DRAW!")

ask_for_window_instruct()
