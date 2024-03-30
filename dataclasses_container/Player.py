import datetime

class Player:
    def __init__(self, player_id, 
                 first_name,last_name,
                 jersey_number,date_of_birth,
                 position,country,team_id):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.jersey_number = jersey_number
        self.date_of_birth = datetime.datetime.fromtimestamp(date_of_birth).strftime('%Y-%m-%d %H:%M:%S')
        self.position = position
        self.country = country
        self.team_id = team_id
    def __repr__(self) -> str:
        return f"ID: {self.player_id} {self.first_name} {self.last_name} Jersey: {self.jersey_number} DOB: {self.date_of_birth} Position: {self.position} Country: {self.country} Team ID: {self.team_id}"
        