import turtle

speed = 20
base = 75
adj = 10
stump_width = 30
stump_height = 50


leaf_colors = ["green", "cyan", "orange", "purple"]
circle_colors = ["gold", "red", "purple", "gray"]
stump_colors = ["brown", "grey", "blue", "cyan"]
tree_x = [-240, 0, 240, 480]


def builder():
    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(3)
    t.speed(speed)
    return t


def turn_lr():
    tina.left(150)
    tommy.right(150)
    tommy.forward(base)
    tina.forward(base)


def turn_rl():
    tommy.left(135)
    tina.right(135)
    tommy.forward(base)
    tina.forward(base)


def leaves(color):
    tina.color(color)
    tommy.color(color)
    tina.pendown()
    tommy.pendown()
    tina.begin_fill()
    tommy.begin_fill()
    tina.forward(base + 25)
    tommy.forward(base + 25)
    for i in range(3):
        turn_lr()
        turn_rl()
    turn_lr()


def circle(color):
    tommy.forward(10)
    tina.forward(10)
    tina.end_fill()
    tommy.end_fill()
    tina.backward(5)
    tommy.backward(5)
    tommy.color("black")
    tina.color("black")
    tina.right(105)
    tommy.left(105)
    tina.forward(50)
    tommy.forward(50)
    tina.color(color)
    tommy.color(color)
    tina.right(90)
    tommy.right(90)
    tina.begin_fill()
    tommy.begin_fill()
    tina.circle(20)
    tina.end_fill()
    tommy.end_fill()


def stump(x, y, color):
    tina.penup()
    tommy.penup()
    tina.goto(x, y)
    tommy.goto(x, y)
    tina.left(180)
    tina.color(color)
    tommy.color(color)
    tina.pendown()
    tommy.pendown()
    tina.begin_fill()
    tommy.begin_fill()
    tina.forward(stump_width / 2)
    tommy.forward(stump_width / 2)
    tina.left(90)
    tommy.right(90)
    tina.forward(stump_height)
    tommy.forward(stump_height)
    tina.left(90)
    tommy.right(90)
    tina.forward(stump_width / 2)
    tommy.forward(stump_width / 2)
    tina.end_fill()
    tommy.end_fill()
    tina.penup()
    tommy.penup()


def full_tree(x, y, leafcolor, circle_color, stump_color):
    leaves(leafcolor)
    circle(circle_color)
    stump(x, y, stump_color)


tina = builder()
tommy = builder()

tommy.left(180)
tina.penup()
tommy.penup()

no_of_trees = len(tree_x)

for i in range(no_of_trees):
    tina.goto(tree_x[i], 0)
    tommy.goto(tree_x[i], 0)
    full_tree(tree_x[i], 0, leaf_colors[i], circle_colors[i], stump_colors[i])


tina.color("green")
tommy.color("green")
tina.goto(-140, 300)
tommy.goto(380, 300)
tommy.left(90)
tina.left(90)
tina.begin_fill()
tommy.begin_fill()
tina.pendown()
tommy.pendown()
tina.forward(50)
tommy.forward(50)
tina.right(90)
tommy.right(90)
tina.forward(520)
tommy.forward(520)
tina.right(90)
tommy.right(90)
tina.forward(50)
tommy.forward(50)
tina.end_fill()
tommy.end_fill()
tommy.right(90)
tommy.forward(230)
tommy.color("black")
tommy.write("Tree Store")
tommy.penup()
tommy.backward(100)


tina.hideturtle()
tommy.hideturtle()
turtle.done()
