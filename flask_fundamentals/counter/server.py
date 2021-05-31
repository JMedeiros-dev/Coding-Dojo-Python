from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'shhh, keep this between us!'


@app.route('/', methods=['POST'])
def keep_count():
    count = 0
    session['plus_two'] = request.form['plus_two']
    session['reset'] = request.form['reset']
    return redirect('/show')


@app.route('/show')
def show_count():
    count = count + 1

    return render_template('show.html', plus_two=session['plus_two'], reset=session['reset'], count=count)


if __name__ == "__main__":
    app.run(debug=True)
