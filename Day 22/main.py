# Day 22 - Pong Game Project

#Import modules
from turtle import Screen
from Paddles import Paddle
from Ball import Game_Ball
from scoreboard import Score
import time,random

#Screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('PONG GAME')

screen.tracer(0)

#Objects
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Game_Ball()
score = Score()


#Listen for keyboard input
screen.listen()
screen.onkeypress(fun=r_paddle.up,key='Up')
screen.onkeypress(fun=r_paddle.down,key='Down')
screen.onkeypress(fun=l_paddle.up,key='w')
screen.onkeypress(fun=l_paddle.down,key='s')


#Variables
is_game_on = True
Moves = ['NE','SE','SW','NW']
Speeds = ['slow','normal','fast','fastest']
speed_count =0.1
direction = random.choice(Moves)


#Game Loop
while is_game_on:
    
    screen.update()
    time.sleep(speed_count)
    ball.move_direction(direction)
    
    
    #Ball Bounce
    if ball.ycor() > 280 and direction == 'NE':
        direction = 'SE'
    if ball.ycor() < -280 and direction == 'SW':
        direction = 'NW'
    if ball.ycor() > 280 and direction == 'NW':
        direction = 'SW'
    if ball.ycor() < -280 and direction == 'SE':
        direction = 'NE'
    
    # Player successfully hit the ball   
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50:
        speed_count *=0.9
            
        if direction == 'NE':
            direction = 'NW'
        else:
            direction = 'SW'
    if ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        speed_count *=0.9
        if direction == 'NW':
            direction = 'NE'
        else:
            direction = 'SE'
            
    # Player fails to hit the ball
    if ball.xcor() > 380:
        speed_count = 0.1
        direction = random.choice(['SW','NW'])
        ball.out_of_bounds()
        score.l_point()
        
    if ball.xcor() < -380:
        speed_count = 0.1
        direction = random.choice(['SE','NE'])
        ball.out_of_bounds()
        score.r_point()
    
    # END GAME CONDITION
    if score.r_score == 5:
        is_game_on = False
        screen.clear()
        screen.bgcolor('black')
        score.game_over('Player 2')
    
    if score.l_score == 5:
        is_game_on = False
        screen.clear()
        screen.bgcolor('black')
        score.game_over('Player 1')

# Exit on click          
screen.exitonclick()