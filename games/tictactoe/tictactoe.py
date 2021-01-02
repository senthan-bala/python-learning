import turtle

z = 100
tina = turtle.Turtle()
tina.shape('turtle')
tina.pensize(3)
tina.speed(20)


# draw big square
tina.goto(z,0)
tina.forward(-3*z)
tina.left(90)
tina.forward(3*z)
tina.right(90)
tina.forward(3*z)
tina.right(90)
tina.forward(3*z)

# up-down lines
tina.right(90)
tina.forward(z)
tina.right(90)
tina.forward(3*z)
tina.left(90)
tina.forward(z)
tina.left(90)
tina.forward(3*z)

# go to top left
tina.right(90)
tina.forward(z)
tina.right(90)
tina.forward(2*z)

# right-left lines
tina.right(90)
tina.forward(3*z)
tina.right(90)
tina.forward(z)
tina.right(90)
tina.forward(3*z)

tina.hideturtle()
turtle.done()