from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=["POST"])
def results():
    name_from_survey = request.form['name']
    location_from_survey = request.form['location']
    language_from_survey = request.form['language']
    comments_from_survey = request.form['comments']
    return render_template("results.html", name=name_from_survey, location=location_from_survey, language=language_from_survey, comments=comments_from_survey)


if __name__ == "__main__":
    app.run(debug=True)
