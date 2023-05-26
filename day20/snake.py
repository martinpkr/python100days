from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.penup()
        turtle.goto(position)
        turtle.color('white')
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].pos())
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            # new_x = self.segments[seg_num - 1].xcor()
            # new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)


    # def check_tail(self):
        # for segment in range(len(self.segments) - 1,0,-1):
        #     print(self.segments[0].pos())
        #     print(self.segments[segment - 1].pos(), 'opashka')
        #     if self.segments[0].pos() == self.segments[segment].pos():
        #         print('problem s opashka')


