from flask import Flask, render_template, url_for, request, session
import libbusstop
app = Flask(__name__)
app.secret_key = "abc123"

# Homepage
@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    session_data = libbusstop.load_data()
    search_term = request.form["q"]
    option = request.form["o"]
    session_data.search_db(search_term, option)
    results = session_data.search_results
    session_data.save_data()
    return render_template("search.html", results=results, len_results=len(results), search_term=search_term)


@app.route("/stop/<atco>/", methods=["POST"])
def next_bus(atco):
    session_data = libbusstop.load_data()
    date = request.form["date"]
    time = request.form["time"]
    time_type = request.form["type"]
    print(date, time, time_type)
    session_data.atco_code = atco
    session_data.get_times(date, time, time_type)
    json_data = session_data.json_data
    session_data.save_data()
    return render_template("next_bus.html", json_data=json_data)


if __name__ == "__main__":
    app.run()
