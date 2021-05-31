from flask import Flask, render_template
app = Flask(__name__,)


@app.route('/')
def index():
    return render_template('index.html', phrase="hello", times=5)


@app.route('/dojo')
def dojo():
    print("ran dojo")
    return 'Dojo!'


@app.route('/say/<name>')
def hello_person(name):
    print("ran person")
    return f"Hello {name}!"


@app.route('/repeat/<int:num>/<str>')
def repeat(num, str):
    sum = str * num
    print(sum)
    return sum


@app.route('/user/<int:user_number>')
def user(user_number):
    return f"You're user #{user_number}!"


@app.route('/play')
def play(times="3", color="blue"):
    print("ran play")
    return render_template("playtimes.html", num_times=int(times), color=color)


@app.route('/play/<times>')
def playtimes(times, color="blue"):
    print("ran play/x")
    return render_template("playtimes.html", num_times=int(times), color=color)


@app.route('/play/<times>/<color>')
def playtimes_color(times, color):
    print("ran play/x/color")
    return render_template("playtimes.html", num_times=int(times), color=color)


@app.errorhandler(404)
def error404(error):
    return "<h1>Sorry! No response. Try again.<h1>", 404


if __name__ == "__main__":
    app.run(debug=True)
