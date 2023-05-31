
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.write('Game Over',align='center',font=('Arial',20,'normal'))
        self.color('black')
        self.penup()
        self.goto(0,0)

    def return_to_start(self):
        self.goto(STARTING_POSITION)