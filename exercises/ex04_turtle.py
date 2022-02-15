"""TODO: Descrobe your scene..."""

__author__ = "730483024"

from turtle import Turtle, colormode, done


def main() -> None: 
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here 
    # TODO: Call the procedures you define and pass your Turtle(s) as your argument.

    done()


def bubbles_random(bubble: Turtle, x: float, y: float, radius: float) -> None:
    "Draw bubbles that have random radii sizes and are located at x, y."
    from random import randint
    radius = randint(5, 20)
    bubble.penup()
    bubble.goto(x, y)
    bubble.setheading(0.0)
    bubble.pendown()
    i: int = 0 
    while i < 360: 
        bubble.fillcolor("light blue")
        bubble.begin_fill()
        bubble.circle(radius)
        bubble.end_fill()
        i += 1


def water_level(line: Turtle, length: int) -> None: 
    """Creating a wavy water level across the sreen."""
    line.penup()
    line.goto(1000, 200)
    line.pendown()
    line.pencolor("blue")
    # is there a way for me to fill blue under the waves?
    i: int = 0
    while i < 5:  # Will not work when I try to iterate but will not work without the wile loop there.
        line.fillcolor("blue")
        line.begin_fill()
        line.setheading(90)
        line.circle(40, 180)
        line.end_fill()
        i += 1  # doesnt work with this here, but will not work without while loop
    while i < 2: 
        line.fillcolor("blue")
        line.begin_fill()
        line.setheading(0.0)
        line.forward(2000)
        line.right(90)
        line.forward(200)
        line.right(90)
        line.end_fill()


def seaweed(height: int, number: int) -> None: 
    """Adding plant life to the bottom floor that vary in height."""


def fish(fish_body: Turtle, length: int) -> None: 
    """Adding a orange fish to my scene."""
    fish_body.circle(30)
    fish_body.circle(30)
    fish_body.pencolor("orange")
    fish_body.penup()
    fish_body.goto(-30, 20)
    fish_body.pendown
    fish_body.setheading(135.0)
    i: int = 0
    while i < 3: 
        fish_body.forward(20)
        fish_body.left(120)
        i += 1


if __name__ == "__main__":
    main()