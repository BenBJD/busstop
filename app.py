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


@app.route("/stop/<atco>/next")
def next_bus(atco):
    session_data = libbusstop.load_data()
    print("now")
    session_data.atco_code = atco
    session_data.get_times(None, None, "next")
    json_data = session_data.json_data
    session_data.save_data()
    route_count = len(json_data["departures"])
    time_count = 0
    for i in json_data["departures"]:
        time_count += len(i)
    return render_template("next_bus.html", json_data=json_data, route_count=route_count, atco=session_data.atco_code)


@app.route("/stop/<atco>/<date>/<time>")
def bus_at(atco, date, time):
    session_data = libbusstop.load_data()
    print(date, time, "specific")
    session_data.atco_code = atco
    session_data.get_times(date, time, "specific")
    json_data = session_data.json_data
    session_data.save_data()
    route_count = len(json_data["departures"])
    time_count = 0
    for i in json_data["departures"]:
        time_count += len(i)
    return render_template("next_bus.html", json_data=json_data, route_count=route_count, atco=session_data.atco_code)


@app.route("/bus/<operator>/<line>/<dir>/<atco>/<date>/<time>")
def line_info(operator, line, date, time):
    session_data = libbusstop.load_data()

    session_data.save_data()


if __name__ == "__main__":
    app.run()
