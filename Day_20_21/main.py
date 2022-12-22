# Day 20_21 - Snake Game Project

from turtle import Screen
from snake import Snake
from score import ScoreBoard
from food import Food
import time

screen = Screen() # need a function for default screen setup

def game():
    '''Initializes main game sequence'''
    screen.setup(width=600, height=600) # need a function for default screen setup
    screen.bgcolor('black')

    user_name = screen.textinput(title="Welcome to Snake Game!", prompt="Type your name: ")
    if user_name:
        screen.title(f'Snake Game : {user_name}')

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
        user_choice = screen.textinput(title=f"Your final score was: {score.count}", prompt="Do you want to play again?(yes/no): ")
        while user_choice == 'yes':
            screen.clear()
            game()
        if user_choice == 'no':
            screen.clear()
            screen.setup(width=600, height=600) # need a function for default screen setup
            screen.bgcolor('black')
            score.thank_you_screen()
            screen.exitonclick()
            
        else:
            screen.clear()
            screen.setup(width=600, height=600) # need a function for default screen setup
            screen.bgcolor('black')
            score.Invalid_screen()
            screen.exitonclick()
        
    else:
        print("Invalid choice!")
        time.sleep(1)
        exit()
        
game()

exit()