from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    input_pass.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = input_website.get()
    if len(website) == 0:
        messagebox.showerror('Invalid input', 'You have an empty entry,try again')
    else:
        try:
            with open('data.json', 'r') as data:
                data_dict = json.load(data)
        except:
            messagebox.showerror(title='No such file',message='There is no created/saved instances yet!')
        else:
            for existing_website in data_dict:
                if existing_website == website:
                    messagebox.showinfo(title='You\'r Credentials',
                                        message=f'Your name and password for {website} are :\n'
                                                f'Email: {data_dict[existing_website]["email"]}\n'
                                                f'Password: {data_dict[existing_website]["password"]}')


def take_data():
    # take the data from inputs
    website = input_website.get()
    email_user = input_email_user.get()
    password = input_pass.get()

    data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showerror('Invalid input', 'You have an empty entry,try again')
    else:
        try:
            with open('./data.json', 'r') as json_data:
                # We load the data that isn't updated
                taken_data = json.load(json_data)

                data.update(taken_data)
        except FileNotFoundError:

            with open('./data.json', 'w') as json_data:
                # We save the update data
                json.dump(data, json_data, indent=4)
        else:
            with open('./data.json', 'w') as json_data:
                # We save the update data
                json.dump(data, json_data, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.config(pady=20, padx=20)
screen.title("Password Manager")
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='./logo.png')

canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# create labels
label_website = Label(text='Website:')
label_email_username = Label(text='Email/Username:')
label_pass = Label(text="Password:")
# grid for labels
label_website.grid(column=0, row=1)
label_email_username.grid(column=0, row=2)
label_pass.grid(column=0, row=3)

# create input fields

input_website = Entry(width=25)
input_email_user = Entry(width=37)
input_email_user.insert(0, 'devilmarti@abv.bg')
input_pass = Entry(width=25)

# grid for input fields
input_website.grid(column=1, row=1, columnspan=1)
input_email_user.grid(column=1, row=2, columnspan=2)
input_pass.grid(column=1, row=3)

# create buttons
search_button = Button(text='Search', command=search,width=7)
generate_pass_buttons = Button(text='Generate', command=gen_pass,width=7)
add_button = Button(text='Add', width=36, command=take_data)

# grid for buttons
search_button.grid(column=2, row=1)
generate_pass_buttons.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()
