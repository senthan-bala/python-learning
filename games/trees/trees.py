import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)

base = 75
adj = 10

num = [base + adj * 2, base + adj, base, base - adj, base - adj * 2]
num2 = [base + adj, base, base - adj, base - adj * 2, base - adj * 3]


def turn_l(position):
    tina.left(55)
    tina.forward(num[position])


def turn_r(pos):
    tina.right(115)
    tina.forward(num2[pos])


tina.begin_fill()
tina.left(90)
tina.goto(base + adj * 2, 0)
turn_l(0)
turn_r(0)
tina.left(90)
turn_l(1)
turn_r(1)
tina.left(90)
turn_l(2)
turn_r(2)
tina.right(90)
tina.circle(20)
tina.right(145)
turn_l(3)
turn_r(3)
tina.left(90)
turn_l(4)
turn_r(4)
tina.left(90)


turtle.done()
