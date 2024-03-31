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
            if self.cursor.fetchone() != None:
                print(f"Match {id} already in database")
                i+=1
                continue
            print(f"Inserting match {i}/{x}")
            self.events_list.all_matches.append(self.events_list.get_match(id))
            i+=1
        for match in self.events_list.all_matches:
            self.cursor.execute(f"INSERT INTO matches (id, date, time, home_team, away_team, home_score, away_score) VALUES ({match.id},'{match.date}','{match.time}','{match.home_team}','{match.away_team}',{match.home_score},{match.away_score})")
        self.connection.commit()

    def insert_players_stats(self):
        for id in self.events_list.all_events_id:
            self.cursor.execute(f"SELECT * FROM player_stats WHERE match_id = {id}")
            if self.cursor.fetchall() != []:
                print(f"Stats for match {id} already in database")
                continue
            print(f"Inserting players stats for match {id}")
            self.events_list.all_players_stats.extend(self.events_list.get_players_stats(id))

        for player in self.events_list.all_players_stats:
            self.cursor.execute(f"INSERT INTO player_stats (match_id, player_id, seconds_played, assists, goals, shots,accuracy) VALUES ({player.match_id},{player.player_id},{player.seconds_played},{player.assists},{player.goals},{player.shots},{player.accuracy})")
        self.connection.commit()


    def is_player_in_db(self,player_id):
        self.cursor.execute(f"SELECT * FROM players WHERE id = {player_id}")
        if self.cursor.fetchone() != None:
            return True
        return False
    
    def add_player_to_db(self,player_id):
        player = self.events_list.get_player_info(player_id)
        print(f"Inserting player {player.first_name} {player.last_name} [ID: {player.id} to database")
        self.cursor.execute(f"INSERT INTO players (id,first_name,last_name,jersey_number,date_of_birth,position,country,team_id) VALUES ({player.id},'{player.first_name}','{player.last_name}',{player.jersey_number},'{player.date_of_birth}','{player.position}','{player.country}',{player.team_id})")
        self.connection.commit()
        
    def __del__(self):
        self.connection.close()