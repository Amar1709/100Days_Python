# Day 20_21 - Snake Game Project

from turtle import Screen
from snake import Snake
from score import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

screen.tracer(0)

snakey = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snakey.up,"Up")
screen.onkey(snakey.down,"Down")
screen.onkey(snakey.right,"Right")
screen.onkey(snakey.left,"Left")


is_game_on = True
score.print_score()

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()
    
    if snakey.head_of_snake.distance(food) < 15:
        food.refresh()
        score.clear()
        score.count+=1
        score.print_score()
        snakey.extend_snake()

    if snakey.head_of_snake.xcor() > 280 or snakey.head_of_snake.xcor() < -280 or snakey.head_of_snake.ycor() > 280 or snakey.head_of_snake.ycor() < -280:
        is_game_on = False
        score.end_game()

    for parts in snakey.snake_body[1:]:
        if snakey.head_of_snake.distance(parts) < 10:
            is_game_on = False
            score.end_game()

screen.exitonclick()