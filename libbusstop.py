import sqlite3
import urllib.request
import json

class GetATCO:
    # Initialising
    def __init__(self, searchTerm, searchTermType):
        self.searchTerm = searchTerm
        self.searchTermType = searchTermType
        conn = sqlite3.connect(naptan_data.db)
        self.cursor = conn.cursor()

    def search(self):
        # Search database for stops with either NaPTAN code or search term
        pass

    def process(self):
        # Format stops into ATCO and location data, then close database connection
        pass

class GetData:
    # Initialising
    def __init__(self, ATCO, searchType):
        self.searchType = searchType
        self.ATCO = ATCO
        self.busService = {
            "inbound": "",
            "outbound": "",
            "fullName": ""
        }

    api_key = "077475e1973c1ff5bb3d52e0ba6e63ca"
    app_id = "b13c7b6d"

    def getOperator(self):
        url = "http://transportapi.com/v3/uk/bus/stop/" + self.ATCO