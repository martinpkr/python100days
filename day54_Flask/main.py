from flask import Flask
import datetime

app = Flask(__name__)

# time_before = datetime.datetime.now()
#
#
# def decorator_time(function):
#     def wrapper_function(*args, **kwargs):
#         function(*args, **kwargs)
#         time = datetime.datetime.now() - time_before
#         print(str(time)[5:])
#     return wrapper_function
#
# @decorator_time
# def multiply(n1, n2):
#     print(n1 * n2)
# @decorator_time
# def print_world():
#     print('Worlds')
#
# multiply(3,2)
# print_world()

def decorator_bold(function):
    def wrapper_function():
        text = function()
        return f'<b>{text}<b>'
    return wrapper_function

def decorator_underline(function):
    def wrapper_function():
        text = function()
        return f'<u>{text}<u>'
    return wrapper_function

def decorator_font(function):
    def wrapper_function():
        text = function()
        return f'<i>{text}<i>'
    return wrapper_function

@app.route('/')
@decorator_bold
@decorator_font
@decorator_underline
def hello_world():
    return 'Hello World!'



@app.route('/bye')
def bye_world():
    return 'Bye'


if __name__ == '__main__':
    app.run(debug=True)
