import mysql.connector
from nhl_requests.Events import Events


class NHL_DB:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='nhl',)
        self.cursor = self.connection.cursor()



    def close_connection(self):
        self.connection.close()