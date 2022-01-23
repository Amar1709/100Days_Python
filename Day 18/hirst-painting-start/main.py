# Day 18 - Hirst painting project

import turtle as t
import random as r


# import colorgram as cg

# rgb_colors = []
# colors = cg.extract('Day 18\hirst-painting-start\image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), 
              (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149),(14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.shape('turtle')
tim.fillcolor('RoyalBlue1')

screen = t.Screen()
screen.colormode(255)

for i in range(10):
    tim.hideturtle()
    tim.penup()
    tim.setpos(-225,-225)
    tim.sety(tim.ycor()+(i*50))
    for j in range(10):
        tim.dot(20,r.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.hideturtle()
        
tim.speed('fast')   
screen.exitonclick()
print(tim)    