from flask import Flask
import datetime

app = Flask(__name__)

time_before = datetime.datetime.now()


def decorator_time(function):
    def wrapper_function(*args, **kwargs):
        function(*args, **kwargs)
        time = datetime.datetime.now() - time_before
        print(str(time)[5:])
    return wrapper_function

@decorator_time
def multiply(n1, n2):
    print(n1 * n2)
@decorator_time
def print_world():
    print('Worlds')

multiply(3,2)
print_world()
@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/bye')
def bye_world():
    return 'Bye'


if __name__ == '__main__':
    app.run()
