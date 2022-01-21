# Turtle Graphics OOP practice

from turtle import Turtle, Screen

tim = Turtle()
print(tim)
tim.shape("turtle")
tim.fillcolor("RoyalBlue")
tim.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
