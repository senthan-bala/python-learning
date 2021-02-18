import turtle

length = 100
tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(100)


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
        x_and_y = input("Please give some coords")
        x, y = x_and_y.split(",")
        if x.isalpha() == True:
            x = x.upper()
            if x == "A" or x == "B" or x == "C":
                if y == "1" or y == "2" or y == "3":
                    y = y.strip()
                    is_x_y_wrong = False
                    return x, y
                else:
                    print("Try Again")
            else:
                print("Try Again")
        else:
            print("Try Again")


def make_circle():


def make_X():


setup(length)
make_board(length)
x, y = ask_coords()


turtle.done()
