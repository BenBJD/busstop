import sqlite3
import urllib.request
import json


class NewRequest:
    def __init__(self):
        self.api_key = "077475e1973c1ff5bb3d52e0ba6e63ca"
        self.app_id = "b13c7b6d"
        self.atco_code = ""
        self.times_data = []
        self.search_results = []

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
