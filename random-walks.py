import random
from turtle import Turtle, Screen


tim = Turtle()

screen = Screen()

screen.colormode(255)


# Generate Random colors and directions
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"]
direction = [0, 90, 180, 270]
tim.pensize(15)


# Create Moves
for moves in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen.exitonclick()