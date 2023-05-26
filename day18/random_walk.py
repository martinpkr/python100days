import turtle
from turtle import Turtle, Screen
from random import *
ran_turtle = Turtle()
turtle.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


angle_list = [90, 180, 270, 360]

for _ in range(300):
    ran_turtle.color(random_color())
    random_dir = choice(angle_list)
    ran_turtle.pensize(10)
    ran_turtle.seth(random_dir)
    ran_turtle.forward(25)

my_screen = Screen()
my_screen.exitonclick()