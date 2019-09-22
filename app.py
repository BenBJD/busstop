from flask import Flask, render_template, url_for, request
import libbusstop
app = Flask(__name__)

# Homepage
@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    search_term = request.form["q"]
    option = request.form["o"]
    search_request = libbusstop.NewRequest(search_term, option)
    results = search_request.search_db()
    print(search_term, option)
    print(results)
    return render_template("search.html", results=results, len_results=len(results), search_term=search_term)


@app.route("/stop/<ATCO>/time/next_bus")
def next_bus(ATCO):
    pass


@app.route("/stop/<ATCO>/time/<time>")
def time_bus(ATCO, time):
    pass


if __name__ == "__main__":
    app.run()
