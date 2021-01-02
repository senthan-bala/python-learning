import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.pensize(3)
tina.speed(100)

colors = {"lime": "#A7E30E", "cyan": "#00ffc4"}

screen = turtle.Screen()
screen.setup(1200, 800)
screen.bgcolor("white")


tina.color("lime")
style = ("black ops one", 20)
tina.write("HELLO,", font=style, align="center")
tina.penup()
tina.right(90)
tina.forward(70)
tina.color(colors["lime"])
style = ("black ops one", 50)
tina.write(" I AM SENTHAN,", font=style, align="center")
tina.forward(70)
style = ("black ops one", 5)
tina.color("purple")
tina.write(" I AM AN ALIEN ", font=style, align="center")
tina.forward(70)
style = ("black ops one", 10)
tina.color("cyan")
tina.write("FROM PLANET", font=style, align="center")
tina.forward(70)
style = ("black ops one", 30)
tina.color("black")
tina.write(" G1373HWY27-SGV3H273C", font=style, align="center")

tina.hideturtle()
turtle.done()
