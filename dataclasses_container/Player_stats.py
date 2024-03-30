class Player_stats:
    def __init__(self, match_id,player_id,
                 seconds_played,assists,
                 goals,shots):
        self.match_id = match_id
        self.player_id = player_id
        self.seconds_played = seconds_played
        self.assists = assists
        self.goals = goals
        self.shots = shots
        self.accuracy = round(goals/shots,2) if shots != 0 else 0

    def __repr__(self) -> str:
        return f"ID: {self.player_id} Match ID: {self.match_id} Goals: {self.goals} Assists: {self.assists} Shots: {self.shots} Accuracy: {self.accuracy} Played: {self.seconds_played} seconds"
