from turtle import Screen, Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    counter = 0
    # snake.check_tail()
    #detect game over if there is collision with a wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
    #Detect collision with food
    if snake.head.distance(food) < 17:
        counter +=1
        food.refresh()
        scoreboard.on_refresh()
        snake.extend()
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    snake.move()

screen.exitonclick()