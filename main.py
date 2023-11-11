from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/temp/<station>/<date>")
def data(station, date):
    return {"station": str(station),
            "date": str(date),
            "temperature": 42}


@app.route("/dictionary/<word>")
def dictionary(word):
    definition = word.capitalize()
    return {"word": word,
            "definition": definition}


if __name__ == "__main__":
    app.run(debug=False)
