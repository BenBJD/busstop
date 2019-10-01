import sqlite3
import urllib.request
import json
from flask import session


def load_data():
    if "atco" in session:
        session_data = NewRequest(session["atco"], session["search_results"], session["json_data"])
    else:
        session_data = NewRequest("", [], [])
    return session_data


class NewRequest:
    def __init__(self, atco, json_data, search_results):
        self.api_key = "077475e1973c1ff5bb3d52e0ba6e63ca"
        self.app_id = "b13c7b6d"
        self.atco_code = atco
        self.json_data = json_data
        self.search_results = search_results

    def search_db(self, search_term, search_term_type):
        conn = sqlite3.connect("naptan_data.db")
        c = conn.cursor()
        self.search_results = []
        # Search database for stops with either naptan code or search term
        if search_term_type == "2":
            c.execute(f"SELECT * FROM stops WHERE NaptanCode = '{search_term}'")
            self.search_results = c.fetchall()
        elif search_term_type == "1":
            c.execute(f"""
            SELECT *
            FROM stops 
            WHERE CommonName LIKE '%{search_term}%'
            OR Landmark LIKE '%{search_term}%'
            OR Street LIKE '%{search_term}%'
            OR LocalityName LIKE '%{search_term}%'
            """)
        for j in c.fetchall():
            j = list(j)
            self.search_results.append(j)
        c.close()
        return

    def get_times(self, date, time, time_type):
        self.json_data = []
        url = []
        if time_type == "next":
            url = f"https://transportapi.com/v3/uk/bus/stop/{self.atco_code}/live.json?api_key={self.api_key}&app_id={self.app_id}"
            print(url)
        elif time_type == "specific":
            url = f"https://transportapi.com/v3/uk/bus/stop/{self.atco_code}/{date}/{time}/timetable.json?api_key={self.api_key}&app_id={self.app_id}"
        json_data = json.load(urllib.request.urlopen(url))
        print(json_data)
        self.json_data = json_data
        return

    def save_data(self):
        session["atco"] = self.atco_code
        session["times_data"] = self.times_data
        session["search_results"] = self.search_results
