import requests
import json
from time import sleep
import sys
sys.path.append("..")
from dataclasses_container.Match import Match
from dataclasses_container.Player_stats import Player_stats
from dataclasses_container.Player import Player
from dataclasses_container.Team import Team

class Events:

    def __init__(self):
        self.API_TIMEOUT = 1
        self.api_headers_common = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        self.main_url = 'https://api.sofascore.com/api/v1/unique-tournament/234/season/52528/events/last/0'
        self.response = requests.get(self.main_url, headers=self.api_headers_common)
        self.all_events_id = [event["id"]for event in self.response.json()["events"]]
        
        self.all_matches = []
        self.all_players_stats = []
        self.all_players_info = []
        self.all_teams_info = []


    def get_match(self,id):
        sleep(self.API_TIMEOUT)
        url = f"https://api.sofascore.com/api/v1/event/{id}"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()["event"]
        match_id = response_json["id"]
        date = response_json["startTimestamp"]
        home_team = response_json["homeTeam"]["name"]
        away_team = response_json["awayTeam"]["name"]
        home_score = response_json["homeScore"]["current"]
        away_score = response_json["awayScore"]["current"]
        
        return Match(match_id, date, home_team, away_team, home_score, away_score)
    
    def get_players_stats(self,match_id):
        result = []
        sleep(self.API_TIMEOUT)
        url = f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()
        home_team = response_json["home"]["players"]
        away_team = response_json["away"]["players"]

        for player in home_team:
            result.append(Player_stats(
                match_id,
                player["player"]["id"],
                player["statistics"]["secondsPlayed"],
                player["statistics"]["assists"],
                player["statistics"]["goals"],
                player["statistics"]["shots"]
            ))
        for player in away_team:
            result.append(Player_stats(
                match_id,
                player["player"]["id"],
                player["statistics"]["secondsPlayed"],
                player["statistics"]["assists"],
                player["statistics"]["goals"],
                player["statistics"]["shots"]
            ))
        return result

    def get_players_info(self,team_id):
        pass


    def get_teams_info(self):
        result = []
        sleep(self.API_TIMEOUT)
        url = "https://api.sofascore.com/api/v1/unique-tournament/234/season/52528/standings/total"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()
        rows = response_json["standings"][6]["rows"]
        for team in rows:
            
            result.append(Team(
                team["team"]["id"],
                team["team"]["name"],
                team["team"]["shortName"],
                team["team"]["nameCode"],
                team["position"],
                team["matches"],
                team["wins"],
                team["losses"],
                team["draws"],
                team["points"]
            ))
        self.all_teams_info = result


