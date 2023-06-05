from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score(score)
    def update_score(self,score):
        self.clear()
        self.write(f"Score: {score}", align='center', move=False, font=('Arial', 22, 'normal'))