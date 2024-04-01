import datetime

class Player:
    def __init__(self, player_id, 
                 name,
                 date_of_birth,
                 position,country,team_id):
        self.id = player_id
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]
        self.date_of_birth = datetime.datetime.fromtimestamp(date_of_birth).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        self.position = position
        self.country = country
        self.team_id = team_id
    def __repr__(self) -> str:
        return f"ID: {self.player_id} {self.first_name} {self.last_name} Jersey: {self.jersey_number} DOB: {self.date_of_birth} Position: {self.position} Country: {self.country} Team ID: {self.team_id}"
        