import sqlite3
import urllib.request
import json


class NewRequest:
    def __init__(self, search_term, search_term_type):
        self.search_term = search_term
        self.search_term_type = search_term_type
        self.atco_code = ""
        self.api_key = "077475e1973c1ff5bb3d52e0ba6e63ca"
        self.app_id = "b13c7b6d"
        conn = sqlite3.connect("naptan_data.db")
        self.c = conn.cursor()

    def search_db(self):
        # Search database for stops with either naptan code or search term
        results = []
        if self.search_term_type == "2":
            self.c.execute(f"SELECT * FROM stops WHERE NaptanCode = '{self.search_term}'")
            results = self.c.fetchall()
        elif self.search_term_type == "1":
            self.c.execute(f"""
            SELECT *
            FROM stops 
            WHERE CommonName LIKE '%{self.search_term}%'
            OR Landmark LIKE '%{self.search_term}%'
            OR Street LIKE '%{self.search_term}%'
            OR LocalityName LIKE '%{self.search_term}%'
            """)
        for j in self.c.fetchall():
            j = list(j)
            del j[4]
            results.append(j)
        # Results saved in "results"
        return results
