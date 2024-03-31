import mysql.connector
from nhl_requests.Events import Events


class NHL_DB:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='nhl_test')
        self.cursor = self.connection.cursor()
        self.events_list = Events()

    def insert_matches(self):
        i = 1
        x = len(self.events_list.all_events_id)
        for id in self.events_list.all_events_id:
            self.cursor.execute(f"SELECT * FROM matches WHERE id = {id}")
            if  self.cursor.fetchone() != None:
                print(f"Match {id} already in database")
                i+=1
                continue
            print(f"Inserting match {i}/{x}")
            self.events_list.all_matches.append(self.events_list.get_match(id))
            i+=1
        for match in self.events_list.all_matches:
            self.cursor.execute(f"INSERT INTO matches (id, date, time, home_team, away_team, home_score, away_score) VALUES ({match.id},'{match.date}','{match.time}','{match.home_team}','{match.away_team}',{match.home_score},{match.away_score})")
        self.connection.commit()

    def __del__(self):
        self.connection.close()