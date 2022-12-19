import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(50)
tina.color("magenta")

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.pensize(3)
tommy.speed(50)
tommy.color("red")

paul = turtle.Turtle()
paul.shape("turtle")
paul.pensize(3)
paul.speed(50)
paul.color("green")

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(3)
bob.speed(50)
bob.color("green")

donald = turtle.Turtle()
donald.shape("turtle")
donald.pensize(3)
donald.speed(50)
donald.color("blue")

tina.right(20)
tina.forward(50)
tommy.left(20)
tommy.forward(50)
bob.right(40)
bob.forward(50)
paul.left(40)
paul.forward(50)
donald.right(180)
donald.forward(50)


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


ask_for_window_instruct()