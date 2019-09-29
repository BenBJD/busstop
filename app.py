from flask import Flask, render_template, url_for, request
import libbusstop
app = Flask(__name__)
global session

# Homepage
@app.route("/")
def homepage():
    session = libbusstop.NewRequest()
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    search_term = request.form["q"]
    option = request.form["o"]
    session.search_db(search_term, option)
    results = session.search_results
    return render_template("search.html", results=results, len_results=len(results), search_term=search_term)


@app.route("/stop/<atco>/", methods=["POST"])
def next_bus(atco):
    date = request.form["date"]
    time = request.form["time"]
    time_type = request.form["type"]
    print(date, time, time_type)
    session.atco_code = atco
    session.get_times(date, time, time_type)
    times_data = session.times_data
    return render_template("next_bus.html", times_data=times_data)


if __name__ == "__main__":
    app.run()
