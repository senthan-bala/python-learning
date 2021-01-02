import turtle

tina = turtle.Turtle()
tina.shape('arrow')
tina.pensize(3)
tina.speed(20)

tina.goto(0,0)
tina.goto(25,25)
tina.goto(0,0)
tina.goto(-25,25)
tina.goto(0,0)
tina.goto(0,-25)
tina.goto(0,0)
tina.penup()
tina.goto(100,0)
tina.pendown()
tina.goto(125,25)
tina.goto(75,25)
tina.penup()
tina.goto(100,0)
tina.pendown()
tina.goto(75,-25)
tina.goto(125,-25)
tina.penup()
tina.goto(-100,0)
tina.pendown()
tina.goto(-125,25)
tina.goto(-75,-25)
tina.goto(-100,0)
tina.goto(-75,25)
tina.goto(-125,-25)
tina.penup()
tina.goto(0,100)

tina.write("This is X,Y,Z!")
tina.goto(-25,100)

turtle.done()




