from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
#get data from file with pandas
try:
    data = pandas.read_csv('./words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
    dict = data.to_dict(orient="records")
else:
    dict = data.to_dict(orient="records")

current_card = {}
#make functions for clicking right and wrong choice buttons


def flip_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    canvas.itemconfig(canvas_image,image=canvas_img)
    canvas.itemconfig(canvas_word_text,text=current_card['French'],fill='black')
    canvas.itemconfig(canvas_title_text,text='French',fill='black')
    flip_timer = window.after(3000, func=next_card)

def right_button():
    flip_card()
    dict.remove(current_card)
    rest_of_data = pandas.DataFrame.from_records(dict)
    rest_of_data.to_csv('words_to_learn.csv')

def next_card():

    canvas.itemconfig(canvas_title_text,text='English', fill='white')
    canvas.itemconfig(canvas_word_text,text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_image,image=canvas_back_img)

window = Tk()
window.minsize(height=400,width=500)
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

#Create main cards
flip_timer = window.after(3000, func=next_card)

canvas = Canvas(width=800,height=526)
canvas_img = PhotoImage(file='./images/card_front.png')
canvas_back_img = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400,263,image=canvas_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_title_text = canvas.create_text(400,150,text='',font=('Ariel',40,'italic'))
canvas_word_text = canvas.create_text(400,263,text='',font=('Ariel',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)

#Create buttons
x_button_img = PhotoImage(file='./images/wrong.png')
x_button = Button(image=x_button_img,command=flip_card)
x_button.grid(column=0,row=1)

right_button_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_img,command=right_button)
right_button.grid(column=1,row=1)

flip_card()

window.mainloop()