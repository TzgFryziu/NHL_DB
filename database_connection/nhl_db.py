import mysql.connector
from nhl_requests.Events import Events


class NHL_DB:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='nhl')
        self.cursor = self.connection.cursor(buffered=True)
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


    def update_teams(self):
        self.events_list.get_teams_info()
        for team in self.events_list.all_teams_info:
            self.cursor.execute(f"SELECT * FROM teams WHERE id = {team.id}")
            if self.cursor.fetchone() != None:
                print(f"Team {team.id} already in database")
                continue
            self.cursor.execute(f"INSERT INTO teams (id, name, short_name, namecode, position, matches, wins, losses, draws, points) VALUES ({team.id},'{team.name}','{team.short_name}','{team.namecode}',{team.position},{team.matches},{team.wins},{team.losses},{team.draws},{team.points})")
        self.connection.commit()

    def update_players(self):
        teams_list = []
        self.cursor.execute("SELECT id FROM teams")
        for team in self.cursor:
            teams_list.append(team[0])
        
        for team in teams_list:
            print(f"Getting players for team {team}")
            self.events_list.get_players_info(team)

        for player in self.events_list.all_players_info:
            self.cursor.execute(f"SELECT * FROM players WHERE id = {player.id}")
            if self.cursor.fetchone() != None:
                print(f"Player {player.id} already in database")
                continue
            #print(f"INSERT INTO players (id, first_name, last_name, jersey_number, date_of_birth, position, country, team_id) VALUES ({player.id},'{player.first_name}','{player.last_name}',{player.jersey_number},'{player.date_of_birth}','{player.position}','{player.country}',{player.team_id})")
            self.cursor.execute(f"INSERT INTO players (id, first_name, last_name, date_of_birth, position, country, team_id) VALUES (%s,%s,%s,%s,%s,%s,%s)", (player.id,player.first_name,player.last_name,player.date_of_birth,player.position,player.country,player.team_id))
        self.connection.commit()
    def __del__(self):
        self.connection.close()