from flask import Flask, render_template, url_for
import urllib.request
import json
import datetime
now = datetime.datetime.now()
app = Flask(__name__)

# Homepage
@app.route("/")
def homepage():
    return render_template('index.html')

# Buses at a stop
@app.route("/stop/<ACIO>/<type>")
def stop_next_bus(ACIO, type):
    if type == "live":
        date_time = "live.json"
    else:
        date_time = type.replace("+", "/") + "/timetable.json"
    url = urllib.request.urlopen("http://transportapi.com/v3/uk/bus/stop/" + ACIO + "/" + date_time + "?app_id=b13c7b6d&app_key=077475e1973c1ff5bb3d52e0ba6e63ca")
    data = json.loads(url.read())
    return data

# Next bus in a line
@app.route("/line/<operator>/<line_num>")
def line_timetable(operator, line_num):
    # Find data from operator and line_num
    return operator

if __name__ == '__main__':
    app.run()
