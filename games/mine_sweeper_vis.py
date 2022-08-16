from random import randint
import turtle
from math import sqrt

pie = turtle.Turtle()
pie.shape("turtle")
pie.pensize(3)
pie.speed(35)
pie.penup()
pie.goto(-250, 250)
map_size = 10
pie.hideturtle()
square_size = 500 / map_size


pallet_not_confirmed=True
while pallet_not_confirmed:
    c_pallet=input("What color pallet do you want?:")
    c_pallet.strip(" ")
    if c_pallet.isalpha()==True:
        pallet_not_confirmed=False
        c_pallet = c_pallet.lower()
        ispallet=False

        while ispallet==False:
            if c_pallet=="normal":
                kill_col="red"
                line_col="black"
                c = "papaya whip"
                colist = [
                    "ivory",
                    "blue",
                    "lime",
                    "red",
                    "deep pink",
                    "maroon",
                    "golden",
                    "gray",
                    "blue violet",
                    "black",
                    "red",
                ]
                ispallet=True
                pallet_not_confirmed=False
            elif c_pallet=="rainbow":
                kill_col="red"
                line_col="white"
                c = "black"
                colist = [
                    "ivory",
                    "red",
                    "orange",
                    "yellow",
                    "green",
                    "aquamarine",
                    "blue",
                    "blue violet",
                    "magenta",
                    "grey",
                    "white",
                ]
                ispallet=True
                pallet_not_confirmed=False
            else:
                ispallet=False
                pallet_not_confirmed=True
                print("please type a valid pallet")
    else:
        pallet_not_confirmed=True
        print("please type a word")



def make_map(map_size, square_size, col, line_c):
    pie.pendown()
    pie.fillcolor(col)
    pie.begin_fill()
    for i in range(4):
        pie.forward(500)
        pie.right(90)
    pie.right(90)
    pie.end_fill()
    pie.color(line_c)
    for i in range(map_size):
        pie.forward(500)
        pie.backward(500)
        pie.left(90)
        pie.forward(square_size)
        pie.right(90)
    pie.right(90)
    pie.forward(500)
    pie.right(180)
    for i in range(map_size):
        pie.forward(500)
        pie.backward(500)
        pie.right(90)
        pie.forward(square_size)
        pie.left(90)
    pie.left(90)
    pie.forward(500)
    pie.right(180)


def check_if_num(subject, map_size):
    for num in range(1, map_size + 1):
        if subject == str(num):
            is_num = True
            return is_num
        else:
            is_num = False
    return is_num


def ready_coords(coords, map_size):
    y, x = coords.split(",")
    x = x.strip(" ")
    y = y.strip(" ")
    isx = check_if_num(x, map_size)
    isy = check_if_num(y, map_size)
    if isx == True:
        x = int(x)
    if isy == True:
        y = int(y)
    return isx, isy, x, y


def open_square(square_size, x, y, map_squares, colist, label):
    zy = int(x)
    zx = int(y)
    rev_label=str(x)+","+str(y)
    mx = zy - 1
    my = zx - 1
    pie.forward(my * square_size)
    pie.left(90)
    pie.forward(mx * square_size)
    pie.fillcolor(colist[map_squares[rev_label]["mines_near"]])
    pie.begin_fill()
    pie.pendown()
    for i in range(5):
        pie.forward(square_size)
        pie.right(90)
    pie.end_fill()
    pie.pencolor("black")
    for i in range(7):
        pie.forward(square_size)
        pie.right(90)
    pie.penup()
    pie.right(90)
    pie.forward(square_size)
    pie.left(90)
    pie.forward(square_size / 4)
    if map_squares[rev_label]["mines_near"] == 0:
        pdjeidj = 560606
    else:
        pie.write(
            str(map_squares[rev_label]["mines_near"]),
            align="left",
            font=("Comic Sans MS", round(square_size * 0.6), "normal"),
        )
    pie.backward(square_size / 4)
    pie.right(90)
    pie.backward(square_size)
    pie.goto(-250, 250)


def flag(x, y, square_size, colist):
    pie.forward((x - 1) * square_size)
    pie.left(90)
    pie.forward((y - 1) * square_size)
    pie.right(90)
    pie.forward(square_size)
    pie.left(90)
    pie.forward(square_size / 4)
    pie.left(90)
    pie.penup()
    pie.forward(square_size / 8)
    pie.pencolor(colist[10])
    pie.pendown()
    pie.forward((square_size / 3) * 2)
    pie.right(110)
    pie.fillcolor(colist[10])
    pie.begin_fill()
    pie.forward(square_size / 2)
    pie.right(140)
    pie.forward(square_size / 2)
    pie.end_fill()
    pie.penup()
    pie.left(70)
    pie.goto(-250, 250)
    pie.color(colist[9])
    flag_marker=True
    return flag_marker


def check_if_flag(x, y, square_size, colist):
    flag_marker=False
    if x[0] == "f":
        if x[1] == "/":
            f, x = x.split("/")
            flag_marker=flag(int(x), y, square_size, colist)
    return flag_marker


def create_map(map_size, square_size):
    map_squares = {}
    for i in range(1, map_size + 1):
        for n in range(1, map_size + 1):
            label = str(i) + "," + str(n)
            map_squares[label] = {}
            map_squares[label]["pos"] = i, n
            map_squares[label]["mine"] = False
    return map_squares


def add_mines(map_squares, map_size):
    mines = []
    not_mines = []
    for x in range(1, map_size + 1):
        for y in range(1, map_size + 1):
            if_mine = randint(1, 6)
            xy = str(y) + "," + str(x)
            if if_mine == 1:
                map_squares[xy]["mine"] = True
                mines.append(xy)
            else:
                not_mines.append(xy)
    return map_squares, not_mines, mines


def check_mines(map_squares, map_size):
    empty_squares = []
    for x in range(1, map_size + 1):
        for y in range(1, map_size + 1):
            if map_squares[str(x) + "," + str(y)]["mine"] == False:
                empty_squares.append(str(x) + "," + str(y))
    return empty_squares


def make_numbers(map_squares, map_size):
    for x in range(1, map_size + 1):
        for y in range(1, map_size + 1):
            mine_number = 0
            label = str(x) + "," + str(y)
            x1 = x + 1
            x2 = x - 1
            y1 = y + 1
            y2 = y - 1
            if x1 < map_size + 1:
                if map_squares[str(x1) + "," + str(y)]["mine"] == True:
                    mine_number += 1
            if y1 < map_size + 1:
                if map_squares[str(x) + "," + str(y1)]["mine"] == True:
                    mine_number += 1
            if x2 > 0:
                if map_squares[str(x2) + "," + str(y)]["mine"] == True:
                    mine_number += 1
            if y2 > 0:
                if map_squares[str(x) + "," + str(y2)]["mine"] == True:
                    mine_number += 1
            if x1 < map_size + 1 and y1 < map_size + 1:
                if map_squares[str(x1) + "," + str(y1)]["mine"] == True:
                    mine_number += 1
            if x1 < map_size + 1 and y2 > 0:
                if map_squares[str(x1) + "," + str(y2)]["mine"] == True:
                    mine_number += 1
            if x2 > 0 and y1 < map_size + 1:
                if map_squares[str(x2) + "," + str(y1)]["mine"] == True:
                    mine_number += 1
            if x2 > 0 and y2 > 0:
                if map_squares[str(x2) + "," + str(y2)]["mine"] == True:
                    mine_number += 1
            map_squares[label]["mines_near"] = mine_number
    return map_squares


def play_game(map_squares, map_size, square_size, colist, not_mines, mines,kfc):
    global opened_squares
    is_game_done = False
    opened_squares = []
    while not is_game_done:
        flag_marker=False
        is_flag = False
        coords = input("What coordinates would you like to search? : ")
        isx, isy, x1, y = ready_coords(coords, map_size)
        if len(str(x1)) >= 3:
            f, x = x1.split("/")
            f = f + "/"
        
        else:
            x = x1

        while not isx or not isy or coords in opened_squares:
            if len(str(x1)) >= 3 and 3 > len(str(y)) > 0:
                is_flag = True
                break
            coords = input("Those coordinates were invalid, please try again: ")
            isx, isy, x, y = ready_coords(coords, map_size)

        if coords[0] == "f":
            pdjeidj = 0
        else:
            win = check_if_win(not_mines, opened_squares)

        label = str(x) + "," + str(y)

        # flag click
        if is_flag == True:
            flag_marker=check_if_flag(x1, y, square_size, colist)
        juycwwwefvc=1
         

        # true cell click

        # lose
        if map_squares[label]["mine"] == True and flag_marker==False:
            print("BOOM! You lose! Maybe next time.")
            end_game(mines, square_size, colist,kfc)
            break

        # win
        if win == True:
            print("You win!")
            open_square(square_size, x, y, map_squares, colist, label)
            break

        kqyewbrckuqy=23

        # normal cell click
        if flag_marker==False:
            print(map_squares[label]["mines_near"])
            open_all(square_size, x, y, map_squares, colist, 0)
            buybjhbyhjbbbbbiaaaaaaaaa=4334
            rev_coords=x,",",y
            jyyvvhuhnhhnhnhnhnhnh=45
            opened_squares.append(rev_coords)


def open_all(square_size, x, y, map_squares, colist, level):
    global opened_squares

    label_a = str(y) + "," + str(x)
    if label_a in opened_squares or map_squares[label_a]["mine"]==True:
        return

    open_square(square_size, x, y, map_squares, colist, label_a)
    open_zeroes(square_size, x, y, map_squares, colist, label_a, level)


def open_zeroes(square_size, x, y, map_squares, colist, label, level):
    global opened_squares

    if map_squares[label]["mines_near"] != 0:
        return

    if label in opened_squares:
        return

    rev_label=str(y)+","+str(x)
    opened_squares.append(rev_label)

    level = level + 1

    x1 = int(x) + 1  
    x0 = int(x) - 1
    y1 = int(y) + 1
    y0 = int(y) - 1

    if x1 < map_size + 1:
        open_all(square_size, x1, y, map_squares, colist, level)
    if y1 < map_size + 1:
        open_all(square_size, x, y1, map_squares, colist, level)
    if x0 > 0:
        open_all(square_size, x0, y, map_squares, colist, level)
    if y0 > 0:
        open_all(square_size, x, y0, map_squares, colist, level)
    if x1 < map_size + 1 and y1 < map_size + 1:
        open_all(square_size, x1, y1, map_squares, colist, level)
    if x1 < map_size + 1 and y0 > 0:
        open_all(square_size, x1, y0, map_squares, colist, level)
    if x0 > 0 and y1 < map_size + 1:
        open_all(square_size, x0, y1, map_squares, colist, level)
    if x0 > 0 and y0 > 0:
        open_all(square_size, x0, y0, map_squares, colist, level)


def end_game(mines, square_size, colist,kfc):
    for mine in mines:
        x, y = mine.split(",")
        x1 = int(y) - 1
        y1 = int(x) - 1
        x2 = x1 * square_size
        y2 = y1 * square_size
        pie.forward(x2)
        pie.left(90)
        pie.forward(y2)
        pie.fillcolor(colist[9])
        pie.begin_fill()
        pie.pendown()
        for i in range(5):
            pie.forward(square_size)
            pie.right(90)
        pie.end_fill()
        pie.color(kfc)
        if mines[0]==mine:
            for i in range(4):
                pie.forward(square_size)
                pie.right(90)
        pie.pendown()
        pie.color(kfc)
        pie.right(45)
        pie.forward(square_size*sqrt(2))
        pie.right(135)
        pie.forward(square_size)
        pie.right(135)
        pie.forward(square_size*sqrt(2))
        pie.right(45)
        pie.penup()
        pie.backward(square_size)
        pie.goto(-250, 250)


def check_if_win(not_mines, opened_squares):
    checked = 0
    not_mine_num = len(not_mines)
    for not_mine in not_mines:
        if_not_in = False
        for opened in opened_squares:
            if not_mine == opened:
                checked += 1
                if_not_in = True
        if if_not_in == False:
            return if_not_in
    if checked == len(not_mines):
        win = True
        return win


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


# def mouse_left(x, y):
#     print("Left => X =", x, "Y =", y)


# def mouse_right(x, y):
#     print("Right => X =", x, "Y =", y)


make_map(map_size, square_size, c, line_col)
map_squares = create_map(map_size, square_size)
map_squares, not_mines, mines = add_mines(map_squares, map_size)
empty_squares = check_mines(map_squares, map_size)
map_squares = make_numbers(map_squares, map_size)
play_game(map_squares, map_size, square_size, colist, not_mines, mines,kill_col)

# turtle.onscreenclick(mouse_left, btn=1)
# turtle.onscreenclick(mouse_right, btn=3)

# ask_for_window_instruct()
turtle.done()