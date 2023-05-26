from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
y = -100
colors = ['red','blue','yellow','green','purple','brown']
all_turtles = []

is_race_on = False

for turtle_index in range(0, 6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 35

user_input = screen.textinput(title='Make your bet',prompt='Bet on what turtle color is gonna win: ')
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_number = random.randint(0,10)
        turtle.forward(random_number)
        if turtle.xcor() >= 250:
            if turtle.color()[0] == user_input:
                screen.textinput(title='you win 100000$',prompt='YOU WIN MADAFKA')
            else:
                screen.textinput(title='you lost :(',prompt='omg cmooon man wtf')




screen.exitonclick()