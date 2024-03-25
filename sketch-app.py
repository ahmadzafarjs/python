from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forword_turtle():
    tim.forward(10)
def backward():
    tim.back(10)
def a_clock():
    tim.left(10)
def clock():
    tim.right(10)

screen.listen()
screen.onkey(key="w", fun=forword_turtle)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=a_clock)
screen.onkey(key="d", fun=clock)
screen.exitonclick()