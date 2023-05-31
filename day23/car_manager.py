from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.random_create()

    def car_move(self,level):
        if level == 1:
            self.forward(random.randint(0,STARTING_MOVE_DISTANCE))
        if level == 2:
            self.forward(random.randint(STARTING_MOVE_DISTANCE + 5,STARTING_MOVE_DISTANCE + MOVE_INCREMENT))
        if level == 3:
            self.forward(random.randint(STARTING_MOVE_DISTANCE + 10, STARTING_MOVE_DISTANCE + 10 + MOVE_INCREMENT))


    def random_create(self):
        self.shape('square')
        self.color(random.choices(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=280, y=random.randint(-280,280))
        self.setheading(180)

    def on_level_up(self):
        self.car_move()