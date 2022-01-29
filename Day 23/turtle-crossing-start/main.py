# Day 23 - Turtle Crossing Game (Capstone Project)

# Import modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

Sleep_time = 0.1

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

#Objects
player = Player()
cars = CarManager()
score_board = Scoreboard()

# Keyboard binding
screen.listen()
screen.onkeypress(player.move_player_Up, 'Up')
screen.onkeypress(player.move_player_Down, 'Down')

# Game Loop
game_is_on = True
while game_is_on:
    time.sleep(Sleep_time)
    screen.update()
    cars.generate_car()
    cars.move_cars()
    
    if player.ycor() >= 280:
        player.reached_finish()
        score_board.increase_score()
        Sleep_time *= 0.5
    
    for car in cars.all_cars:
        if player.distance(car) < 30:
            score_board.game_over()
            game_is_on = False
        


screen.exitonclick()