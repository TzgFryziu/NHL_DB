import datetime

class Match:

    def __init__(self, match_id, date, 
                 home_team, away_team, home_score, 
                 away_score):
        
        self.id = match_id
        self.date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        self.time = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S').split(" ")[1]
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
    
    def __repr__(self) -> str:
        return f"ID: {self.match_id} Date: {self.date} {self.home_team} {self.home_score} - {self.away_team} {self.away_score}"
