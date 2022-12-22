# Day 19 - Turtle Race Project

from turtle import Turtle, Screen
import random


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_boys = [] #List of turtle objects
is_race_on = False #while loop control condition
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which Turtle will win the race? Enter a color : ")

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.fillcolor(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-150 +(60*i)))
    turtle_boys.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in turtle_boys:
        if turtles.xcor() >=230: # if a turtle reaches the finish line
            winner = turtles.fillcolor()
            if user_bet == winner:
                print("\nYou WIN!")
            else:
                print("\nSorry You LOSE!")
            print(f"\n{winner.upper()} Turtle is the Winner!")
            is_race_on = False
            break
        else:  # move random distances 
            random_dist = random.randint(0,10)
            turtles.forward(random_dist)

screen.exitonclick()