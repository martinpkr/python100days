from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

#make a text turtle that displays the score it needs to start from zero!

    def __init__(self):
        super().__init__()
        self.score_counter = 0
        self.penup()
        self.goto(x=0, y=260)
        self.up_one()
        self.hideturtle()

    def up_one(self):
        self.clear()
        self.score_counter += 1
        self.write(f'Score {self.score_counter}', move=False, align='center', font=FONT)
