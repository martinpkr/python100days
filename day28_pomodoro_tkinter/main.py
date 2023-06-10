from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNT = 0
reps = 0
checkmarks = '✔'
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 1
    start_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    pomodoro_work_time = WORK_MIN * 60
    pomodoro_break_time = SHORT_BREAK_MIN * 60
    pomodoro_long_break_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0 and reps != 0:
        label.config(text='Finish/Long Break', fg=RED, font=(FONT_NAME, 28, 'bold'), bg=YELLOW, highlightthickness=0)
        counter(pomodoro_long_break_time)
        reps = 0
    elif reps % 2 == 0:
        counter(pomodoro_work_time)
        reps += 1
    elif reps % 2 == 1:
        label.config(text='Break',fg=PINK,font=(FONT_NAME,28,'bold'),bg=YELLOW,highlightthickness=0)
        counter(pomodoro_break_time)
        reps += 1
    else:
        pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):

    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds > 10:
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    else:
        canvas.itemconfig(timer_text, text=f'{count_min}:0{count_seconds}')

    if count > 0:
        window.after(1000,counter,count-1)
    else:
        var = checkmarks + '✔'
        if reps % 2 == 1:
            checkmark.config(text=f'{var}',fg=GREEN,font=(FONT_NAME,28,'bold'),bg=YELLOW,highlightthickness=0)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00',font=(FONT_NAME,18,'bold'))
canvas.grid(column=1, row=1)


label = Label(text='Timer',fg=GREEN,font=(FONT_NAME,28,'bold'),bg=YELLOW,highlightthickness=0)
label.grid(column=1,row=0)

start_button = Button(text='Start',command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark = Label(text='✔',fg=GREEN,font=(FONT_NAME,28,'bold'),bg=YELLOW,highlightthickness=0)
checkmark.grid(column=1,row=3)





window.mainloop()