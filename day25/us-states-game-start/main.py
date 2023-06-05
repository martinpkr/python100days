from turtle import Turtle, Screen
import pandas
from state_turtle import TextTurtle
from scoreboard import Scoreboard
data = pandas.read_csv('50_states.csv')
states_list = data["state"].to_list()
already_guessed_states = []
score_count = 0


screen = Screen()
turtle = Turtle()
score = Scoreboard(0)

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

screen.title('Guess the USA States')
for instance in states_list:
    user_input = screen.textinput(title='Guess a state',prompt='Type the name of a USA state')
    if user_input in states_list and user_input not in already_guessed_states:
        score_count += 1
        score.update_score(score_count)
        already_guessed_states.append(user_input)
        row = data[data['state'] == user_input]
        print(row.x,row.y)
        text = TextTurtle(str(user_input),int(row.x),int(row.y))


screen.mainloop()

