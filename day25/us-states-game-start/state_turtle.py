from turtle import Turtle

class TextTurtle(Turtle):
    def __init__(self,text,xcor,ycor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(xcor,ycor)
        self.write(f"{text}", move=True,font=('Arial', 13, 'normal'))
