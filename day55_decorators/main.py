from flask import Flask
import random
app = Flask(__name__)

random_num = random.randint(1,9)

@app.route('/')
def home_route():
    return '<h1>Guess a number between 1 - 9 !</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp">'

@app.route(f'/<int:number>')
def correct_route(number):
    if number == random_num:
        return '<h1 style=color:red>You Guessed Right!</h1>' \
               '<img src="https://media4.giphy.com/media/5i7umUqAOYYEw/giphy.gif?cid=ecf05e4782g3w8xieni5m7whlwggc39dsw4hjqwq90bosn4w&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif number > random_num:
        return '<h1 style=color:blue>You Guessed Too High!</h1>' \
               '<img src="https://media0.giphy.com/media/CIpaaClprJ4LC/giphy.gif?cid=ecf05e47095uvs0hueyjv5k7ebud6t12ls7xfa84bvirn96k&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
    elif number < random_num:
        return '<h1 style=color:pink>You Guessed Too Low!</h1>' \
               '<img src="https://media3.giphy.com/media/cveYIL5nqZXM15lOmk/giphy.gif?cid=ecf05e47wdcmh57fhj352sevbnact4fwl8igu87ankfbtd4n&ep=v1_gifs_search&rid=giphy.gif&ct=gx">'


if __name__ == '__main__':
    app.run(debug=True)