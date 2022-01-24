# Day 19 - Etch a Sketch project

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape('turtle')
tim.fillcolor('RoyalBlue1')
tim.pensize(5)
tim.pencolor((160,32,240))


def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(10)
    
def turn_left():
    tim.left(10)
    
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim.speed('fastest')
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="space", fun=clear_drawing)
screen.exitonclick()