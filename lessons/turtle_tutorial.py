"""Turtle Tutorial"""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.circle(30)

leo.pencolor("orange")
leo.penup()
leo.goto(-30, 20)
leo.pendown
leo.setheading(135.0)
leo.forward(20)
leo.left(120)
leo.forward(20)
leo.left(120)
leo.forward(20)
leo.left(120)


# i: int = 0

# leo.speed(50)
# leo.hideturtle()
# leo.pencolor("pink")
# leo.fillcolor(250, 250, 250)
# leo.goto(-150, -100)

# leo.begin_fill()
# while i < 3:
#     leo.forward(300)
#     leo.left(120)
#     i += 1
# leo.end_fill()

# leo.penup()
# leo.goto(-100, 200)
# leo.pendown()
# leo.fillcolor("blue")
# leo.setheading(0.0)
# leo.begin_fill()
# leo.forward(2000)
# leo.end_fill()


# leo.circle(80, steps=3)
# leo.penup()
# leo.forward(200)
# leo.pendown()
# leo.right(30)
# leo.forward(100)

# bob: Turtle = Turtle()
# bob.pencolor(1, 1, 1)
# bob.speed(55)
# side_length: float = 300
# bob.penup()
# bob.goto(-150, -100)
# bob.pendown()

# i: int = 0
# while i < 3:
#     bob.forward(side_length)
#     bob.left(120)
#     i += 1


# i: int = 0
# while i < 70:
#     side_length = side_length * 0.95
#     bob.forward(side_length)
#     bob.left(123)
#     i += 1


done()