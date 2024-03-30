class Team:
    def __init__(self,id,name,
                 short_name,namecode,
                 stadium):
        self.id = id
        self.name = name
        self.short_name = short_name
        self.namecode = namecode
        self.stadium = stadium
    def __repr__(self) -> str:
        return f"ID: {self.id} Name: {self.name} Short Name: {self.short_name} Name Code: {self.namecode} Stadium: {self.stadium}"