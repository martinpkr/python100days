from tkinter import *

# def command():
#     string = input.get()
#     my_lable.config(text=string)
#
# window = Tk()
# window.title('First GUI Program')
# window.minsize(width=500,height=300)
#
# my_lable = Label(text="I am lable",font=("Arial",18,"bold"))
# my_lable.grid(column=0,row=0)
#
# my_button = Button(text='Button',command=command)
# my_button.grid(column=1,row=1)
#
# new_button = Button(text='New Button')
# new_button.grid(column=3,row=0)
#
# input = Entry()
# input.grid(column=4,row=4)
def miles_to_km():
    number = input.get()
    kilometers = int(number) * 1.6
    text.config(text=f'{round(kilometers)}')
window = Tk()
window.title('Miles to Kilometers')
window.minsize(width=400,height=250)

input = Entry(width=10)
input.grid(row=1,column=1)
input_lable = Label(text='miles')
input_lable.grid(row=1,column=2)

is_equal_label = Label(text='is equal')
is_equal_label.grid(row=2,column=0)
text = Label(text='',font=('Arial',12,'bold'))
text.grid(row=2,column=1)

button = Button(text='Convert',command=miles_to_km)
button.grid(row=3,column=1)



window.mainloop()