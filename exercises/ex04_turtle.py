"""A beautiful underwater scene with bubbles, seaweed, and one orange fish. I attempted to place the seaweed and bubbles in randomized areas, so that every time you call the main function, it will be unique!"""

__author__ = "730483024"

from turtle import Turtle, colormode, done
# Why is there a colormode error? Do I need to do the numbers?
# is all this hard coding bad?
# do I have enough functions?


def main() -> None: 
    """The entrypoint of my scene."""
    t: Turtle = Turtle()
    t.speed(0)
    t.hideturtle()
    x: int = 0
    y: int = 0
    t.screen.bgcolor("blue")
    seaweed(t, x, y)
    bubbles_random(t, x, y)
    # fish(t, x, y)
    double(t, x, y)
    done()


def bubbles_random(t: Turtle, x: float, y: float) -> None:
    "Draw bubbles that have random radii sizes and are located at x, y."
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
    """Adding plant life to the bottom floor that vary in height."""
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
    t.setheading(0)
    t.backward(30)
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


def double(t: Turtle, x: float, y: float):  # THIS IS PROBLEMATIC. Doesn't do exact copy
    """A function to make two fish."""
    i: int = 0
    from random import randint
    while i < 2:
        print(fish(t, randint(-300, 300), randint(-300, 300)))
        i += 1


if __name__ == "__main__":
    main()