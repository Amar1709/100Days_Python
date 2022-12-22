# pylint: disable=E1101

# Day 25 - Python - Practice _ US States Game Project

from turtle import Turtle,Screen
import pandas as pd

Font = ('Courier', 8, 'normal')
Align = 'Center'
score = 0
df = pd.read_csv("Day 25/us-states-game-start/50_states.csv")

df2_state = df.state.to_list()
df2_x = df.x.to_list()
df2_y = df.y.to_list()

for item in df2_state:
    df2_state[df2_state.index(item)] = item.lower()

new_turtle = Turtle()
screen = Screen()
screen.title("US State Game")
screen.setup(width=800, height=600)
image = "Day 25/us-states-game-start/blank_states_img.gif"

screen.addshape(image)
new_turtle.shape(image)
is_playing = True

correct_guesses = []

while is_playing:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.lower()
    #print(answer_state)
    
    if answer_state == 'exit':
        break
    
    if answer_state in df2_state:
        temp_turtle = Turtle()
        temp_turtle.hideturtle()
        temp_turtle.penup()
        temp_turtle.goto(df2_x[df2_state.index(answer_state)], df2_y[df2_state.index(answer_state)])
        temp_turtle.write(answer_state.upper(), font=Font, align=Align)
        score+=1
        correct_guesses.append(answer_state)
        df2_state.remove(answer_state)
    
    if score == 50:
        is_playing = False
        screen.textinput(title="Congratulations", prompt="You win!\n\nPress any key to exit")
        break

# States that were guessed correctly
correct_guesses = pd.DataFrame(correct_guesses)
correct_guesses.to_csv("Day 25/us-states-game-start/correct_guesses.csv")

# States that were missed 
df2_state = pd.DataFrame(df2_state)
df2_state.to_csv("Day 25/us-states-game-start/missed_guesses.csv")