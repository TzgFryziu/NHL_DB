class Odds:
    def __init__(self,match_id,
                 home,away,draw,
                 over_4_5,over_5_5,
                 over_6_5,under_4_5,
                 under_5_5,under_6_5):
        self.match_id = match_id
        self.home = home
        self.away = away
        self.draw = draw
        self.over_4_5 = over_4_5
        self.over_5_5 = over_5_5
        self.over_6_5 = over_6_5
        self.under_4_5 = under_4_5
        self.under_5_5 = under_5_5
        self.under_6_5 = under_6_5