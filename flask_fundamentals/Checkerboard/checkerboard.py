from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index(x=4, y=4):
    return render_template("index.html", x=int(x), y=int(y))


@app.route('/<x>')
def for_x(x, y=4):
    return render_template("index.html", x=int(x), y=int(y))


@app.route('/<x>/<y>')
def for_xy(x, y):
    return render_template("index.html", x=int(x), y=int(y))


@app.route('/<x>/<y>/<color1>/<color2>')
def for_color(x, y):
    return render_template("index.html", x=int(x), y=int(y))


if __name__ == "__main__":
    app.run(debug=True)
