from tkinter import  *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)




    password_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    input_pass.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

#take the data from inputs
def take_data():
    website = input_website.get()
    email_user = input_email_user.get()
    password = input_pass.get()
    print(len(website),len(email_user),len(password))
    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showerror('Invalid input','You have an empty entry,try again')
    else:
        is_ok = messagebox.askyesno(title=website,message=f'Email:{email_user}\nPassword: {password}\n is it okay to save ?')
        if is_ok:
            with open('./data.text', 'a') as data:
                data.write(f"\n{website} | {email_user} | {password}")
                data.close()


    input_website.delete(0,END)
    input_pass.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.config(pady=20,padx=20)
screen.title("Password Manager")
canvas = Canvas(width=200,height=200)
img = PhotoImage(file='./logo.png')

canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

#create labels
label_website = Label(text='Website:')
label_email_username = Label(text='Email/Username:')
label_pass = Label(text="Password:")
# grid for labels
label_website.grid(column=0,row=1)
label_email_username.grid(column=0,row=2)
label_pass.grid(column=0,row=3)

#create input fields

input_website = Entry(width=35)
input_email_user = Entry(width=35)
input_email_user.insert(0,'devilmarti@abv.bg')
input_pass = Entry(width=21)

# grid for input fields
input_website.grid(column=1,row=1,columnspan=2)
input_email_user.grid(column=1,row=2,columnspan=2)
input_pass.grid(column=1,row=3)

# create buttons
generate_pass_buttons = Button(text='Generate Password',command=gen_pass)
add_button = Button(text='Add',width=36,command=take_data)

# grid for buttons

generate_pass_buttons.grid(column=2,row=3)
add_button.grid(column=1,row=4,columnspan=2)




screen.mainloop()