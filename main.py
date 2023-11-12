from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

dictionary_df = pd.read_csv('dictionary.csv')

stations_df = pd.read_csv("data_small/stations.txt", skiprows=17)


@app.route("/")
def index():
    return render_template("index.html", data=stations_df[0:92].to_html())


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/api_v1/temp/<station>")
def temp_station(station):
    station_name = station.zfill(6)
    df = pd.read_csv(f"data_small/TG_STAID{station_name}.txt", skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result


@app.route("/api_v1/temp/<station>/<year>")
def temp_station_year(station, year):
    station_name = station.zfill(6)
    df = pd.read_csv(f"data_small/TG_STAID{station_name}.txt", skiprows=20, parse_dates=['    DATE'])
    df = df.loc[df['    DATE'].dt.year == int(year)]
    result = df.to_dict(orient="records")
    return result


@app.route("/api_v1/temp/<station>/<year>/<month>/<day>")
def temp_station_date(station, year, month, day):
    date = year + month + day
    station_name = station.zfill(6)
    df = pd.read_csv(f"data_small/TG_STAID{station_name}.txt", skiprows=20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": str(station),
            "date": str(date),
            "temperature": str(temp)}


@app.route("/api_v1/dictionary/<word>")
def dictionary(word):
    definition = dictionary_df.loc[dictionary_df['word'] == word]['definition'].squeeze()
    return {"word": word,
            "definition": definition}


if __name__ == "__main__":
    app.run(debug=False)
