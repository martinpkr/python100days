THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
import html
quiz = QuizBrain(question_data)

class QuizInterface:


    def __init__(self,quiz: QuizBrain):
        self.Quizbran = QuizBrain(question_data)

        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(pady=20,padx=20,background=THEME_COLOR)


        self.canvas = Canvas(width=300,height=250,background='white')
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)
        self.text = self.canvas.create_text(150,125,text='')

        self.button_img = PhotoImage(file='images/true.png')
        self.button_right = Button(image=self.button_img,pady=20,padx=20,command=self.right_answer)
        self.button_right.grid(column=0,row=2)

        self.button_img2 = PhotoImage(file='images/false.png')
        self.button_false = Button(image=self.button_img2,pady=20,padx=20,command=self.false_answer)
        self.button_false.grid(column=1,row=2)


        self.label = Label(text=f'Score: ')
        self.label.grid(column=1,row=0)
        self.change_question()
        self.window.mainloop()

    def split_string(self,string):
        words = string.split()
        lines = [" ".join(words[i:i + 6]) for i in range(0, len(words), 5)]
        return "\n".join(lines)
    def change_question(self):
        self.canvas.config(bg='white')
        quiz.next_question()
        self.splitted = html.unescape(self.split_string(quiz.current_question['question']))
        self.canvas.itemconfig(self.text,text=self.splitted)

    def right_answer(self):

        is_right = quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_answer(self):

        is_false = quiz.check_answer('false')
        self.give_feedback(is_false)
    def give_feedback(self,bool):
        if bool:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.change_question)



