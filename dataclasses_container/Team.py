class Team:
    def __init__(self,id,name,
                 short_name,namecode,position,matches,
                 wins,losses,draws,points):
        self.id = id
        self.name = name
        self.short_name = short_name
        self.namecode = namecode
        self.position = position
        self.matches = matches
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points
    def __repr__(self) -> str:
        return f"ID: {self.id} Name: {self.name} Short Name: {self.short_name} Name Code: {self.namecode} Stadium: {self.stadium}"