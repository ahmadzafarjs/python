import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)

direction = 0
def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(30):
    tim.speed(10)
    direction += 15
    tim.pencolor(rgb())
    tim.setheading(direction)
    tim.circle(60)

screen.exitonclick()