import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# make turtle with turtle shape
player = Player()
car = CarManager()
# make the turtle move on the x-axis when 'up' key is pressed
screen.onkey(player.move, 'Up')
score = Scoreboard()

#make impact on collision with card

#level up and maybe make the time.sleep + 0.1 on every new level
game_is_on = True
count = 0
score_count = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    if player.ycor() >= 280:
        score.up_one()
        player.return_to_start()
        score_count += 1
    if count % 10 == 0:
        # spawn random number of cars that begin in the y-axis and move to the end
        car = CarManager()
        cars.append(car)
    for index, t in enumerate(cars):
        t.car_move(score_count)
        if t.distance(player) < 20:
            player.game_over()
            screen.reset()



