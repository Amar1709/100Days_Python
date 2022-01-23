# Day 18 _ turtle graphics practice

from turtle import Turtle, Screen
from random import randint
import turtle

from matplotlib.pyplot import draw

tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)

tim.pensize(2)
tim.fillcolor('RoyalBlue1')

# Challenge 1 - Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2 - Draw a dashed line
# for i in range (10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3 - Draw different shapes
# for i in range (3,11):
#     tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
#     for j in range (i):
#         tim.forward(100)
#         tim.right(int(360/i))

# Challenge 4 - Random Walk (Another way to do it listed at the end)

# def go_up(step_size):
#     tim.setheading(90)
#     tim.forward(step_size)

# def go_right(step_size):
#     tim.setheading(0)
#     tim.forward(step_size)
    
# def go_left(step_size):
#     tim.setheading(180)
#     tim.forward(step_size)
    
# def go_down(step_size):
#     tim.setheading(270)
#     tim.forward(step_size)
    
# def move_random_direction(step_size,step_number):
#     move_dir = {1:go_up,2:go_right,3:go_left,4:go_down}
    
#     for i in range(step_number):
        
#         tim.color(randint(0,255),randint(0,255),randint(0,255))
        
#         move_some_dir = move_dir[randint(1,4)]
#         move_some_dir(step_size)

tim.speed("fastest")
# move_random_direction(15,200)

# Challenge 5 - Spirograph
def draw_spirograph(turn_gap):
    for i in range(int(360/turn_gap)):
        tim.color(randint(0,255),randint(0,255),randint(0,255))
        tim.circle(radius=100)
        tim.left(turn_gap)
        tim.hideturtle()
draw_spirograph(10)
screen.exitonclick()
    
print(tim)
