from random import randint
import turtle

pie = turtle.Turtle()
pie.shape("turtle")
pie.pensize(3)
pie.speed(35)
pie.penup()
pie.goto(-250, 250)
map_size = 10
square_size = 500 / map_size
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


def make_map(map_size, square_size, col):
    pie.pendown()
    pie.fillcolor(col)
    pie.begin_fill()
    for i in range(4):
        pie.forward(500)
        pie.right(90)
    pie.right(90)
    pie.end_fill()
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
    x, y = coords.split(",")
    x = x.strip()
    y = y.strip()
    isx = check_if_num(x, map_size)
    isy = check_if_num(y, map_size)
    if isx == True:
        x = int(x)
    if isy == True:
        y = int(y)
    return isx, isy, x, y


def open_square(square_size, x, y, map_squares, colist, label):
    mx = x - 1
    my = y - 1
    pie.forward(mx * square_size)
    pie.left(90)
    pie.forward(my * square_size)
    pie.fillcolor(colist[map_squares[label]["mines_near"]])
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
    pie.write(
        str(map_squares[label]["mines_near"]),
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


def check_if_flag(x, y, square_size, colist):
    if x[0] == "f":
        if x[1] == "/":
            f, x = x.split("/")
            flag(int(x), y, square_size, colist)


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
            xy = str(x) + "," + str(y)
            while xy in mines:
                xy = str(x) + "," + str(y)
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


def play_game(map_squares, map_size, square_size, colist, not_mines, mines):

    is_game_done = False
    opened_squares = 0
    while not is_game_done:
        is_flag = False
        coords = input("What coordinates would you like to search? : ")
        isx, isy, x1, y = ready_coords(coords, map_size)
        if len(str(x1)) >= 3:
            f, x = x1.split("/")
            f = f + "/"
        else:
            x = x1
        while not isx or not isy:
            if len(x1) >= 3 and 3 > len(str(y)) > 0:
                is_flag = True
                break
            coords = input("Those coordinates were invalid, please try again: ")
            isx, isy, x, y = ready_coords(coords, map_size)
        label = str(x) + "," + str(y)
        if is_flag == True:
            check_if_flag(x1, y, square_size, colist)
        elif map_squares[label]["mine"] == True:
            print("BOOM! You lose! Maybe next time.")
            end_game(mines, square_size, colist)
            break
        elif len(not_mines) == opened_squares:
            print("You win!")
            open_square(square_size, x, y, map_squares, colist, label)
            break

        else:
            print(map_squares[label]["mines_near"])
            opened_squares = opened_squares + 1
            open_square(square_size, x, y, map_squares, colist, label)


def end_game(mines, square_size, colist):
    for mine in mines:
        pie.pendown()
        x, y = mine.split(",")
        x1 = int(x) - 1
        y1 = int(y) - 1
        x2 = x1 * square_size
        y2 = y1 * square_size
        pie.forward(x2)
        pie.left(90)
        pie.forward(y2)
        pie.fillcolor(colist[9])
        pie.begin_fill()
        for i in range(5):
            pie.forward(square_size)
            pie.right(90)
        pie.end_fill()
        pie.penup()
        pie.goto(-250, 250)


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


make_map(map_size, square_size, c)
map_squares = create_map(map_size, square_size)
map_squares, not_mines, mines = add_mines(map_squares, map_size)
empty_squares = check_mines(map_squares, map_size)
map_squares = make_numbers(map_squares, map_size)
play_game(map_squares, map_size, square_size, colist, not_mines, mines)

ask_for_window_instruct()
turtle.done()