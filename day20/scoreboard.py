from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.color('white')
        self.penup()
        self.width()
        self.hideturtle()
        self.setpos(x=0, y=280)
        self.update()

    def update(self):
        self.write(arg=f'Score: {self.i}', move=False, align='center', font=('Arial,', 12, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', move=False, align='center', font=('Arial,', 12, 'normal'))

    def on_refresh(self):
        self.i += 1
        self.clear()
        self.update()

