import sqlite3
import urllib.request
import json
from flask import session


def load_data():
    if "session_data" in session:
        session_data = NewRequest(session["atco"], session["], session[""])
        session_data = session["session_data"]
    else:
        session_data = NewRequest("", [], [])
    return session_data


def save_data(session_data):
    session["atco"] = session_data.atco_code
    session["times_data"] = session_data.times_data
    session["search_results"] = session_data.search_results


class NewRequest:
    def __init__(self, atco, times_data, search_results):
        self.api_key = "077475e1973c1ff5bb3d52e0ba6e63ca"
        self.app_id = "b13c7b6d"
        self.atco_code = atco
        self.times_data = times_data
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
        self.times_data = []
        pass
