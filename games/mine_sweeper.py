from random import randint
# from pygame import mixer 
import os
map_size = 10
# mixer.init()



def check_if_num(subject, map_size):
    for num in range(1, map_size - 1):
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


def make_map(map_size):
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
    mine_amt = randint(map_size - 1, map_size + 1)
    for mine in range(1, mine_amt + 1):
        x = str(randint(1, map_size))
        y = str(randint(1, map_size))
        xy = x + "," + y
        while xy in mines:
            x = str(randint(1, map_size))
            y = str(randint(1, map_size))
            xy = x + "," + y
        map_squares[xy]["mine"] = True
        mines.append(xy)
    return map_squares


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


def play_game(map_squares, map_size):
    # lose_sound=mixer.Sound(os.path.join("pygame_stuff\\womp-womp.zip"))
    is_game_done = False
    while not is_game_done:
        coords = input("What coordinates would you like to search? : ")
        isx, isy, x, y = ready_coords(coords, map_size)
        while not isx or not isy:
            coords = input("Those coordinates were invalid, please try again: ")
            isx, isy, x, y = ready_coords(coords, map_size)
        label = str(x) + "," + str(y)
        if map_squares[label]["mine"] == True:
            # lose_sound.play()
            print("BOOM! You lose! Maybe next time.")
            break
        else:
            print(map_squares[label]["mines_near"])


map_squares = make_map(map_size)
map_squares = add_mines(map_squares, map_size)
map_squares = make_numbers(map_squares, map_size)
play_game(map_squares, map_size)
