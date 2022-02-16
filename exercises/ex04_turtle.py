"""A beautiful underwater scene with bubbles, seaweed, and one orange fish. The seaweed, fish, and bubbles in randomized areas, so every time the scene is unique!"""

__author__ = "730483024"

from turtle import Turtle, done


def main() -> None: 
    """The entrypoint of my scene."""
    t: Turtle = Turtle()
    u: Turtle = Turtle()
    t.speed(0)
    t.hideturtle()
    u.speed(0)
    u.hideturtle()
    x: int = 0
    y: int = 0
    t.screen.bgcolor("blue")
    seaweed(t, x, y)
    bubbles_random(t, x, y)
    double(t, u)
    done()


def bubbles_random(t: Turtle, x: float, y: float) -> None:
    "Draw bubbles that have random radii sizes and are located in random spots on the scene."
    i: int = 0 
    while i < 30: 
        from random import randint
        radius = randint(5, 20)
        t.penup()
        t.goto(x, y) 
        t.setheading(0.0)
        t.pendown()
        t.pencolor("light blue")
        t.fillcolor("light blue")
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        x = randint(-700, 700)
        y = randint(-300, 400)
        i += 1


def seaweed(t: Turtle, x: float, y: float) -> None: 
    """Adding plant life to the bottom floor that vary in height and where they grow."""
    i: int = 0
    height: int = 60
    from random import randint
    while i < 10:
        t.penup()
        t.goto(randint(-700, 700), -450)
        t.pendown()
        t.setheading(0)
        t.left(90)
        t.forward(25)
        t.left(45)
        t.pencolor("black")
        t.fillcolor("green")
        t.begin_fill()
        height = randint(-150, -80)
        t.circle(height, 90)
        t.right(90)
        t.circle(height, 90)
        t.end_fill()
        t.right(135)
        t.forward(70)
        t.left(180)
        i += 1


def fish(t: Turtle, x: float, y: float) -> None: 
    """Adding a orange fish to my scene."""
    t.color("orange", "orange")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.setheading(180)
    t.forward(30)
    t.setheading(90.0)
    t.forward(30)
    t.pendown()
    t.setheading(135.0)
    i: int = 0
    t.begin_fill()
    while i < 3: 
        t.forward(50)
        t.left(120)
        i += 1
    t.end_fill()


def double(t: Turtle, u: Turtle):
    """A function to make two fish."""
    i: int = 0
    from random import randint
    while i < 2:
        if i == 0: 
            fish(t, randint(-600, 300), randint(-200, 300))
        else:
            fish(u, randint(350, 650), randint(-200, 300))
        i += 1


if __name__ == "__main__":
    main()