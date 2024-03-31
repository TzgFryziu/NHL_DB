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

    def get_player_info(self,id):
        sleep(self.API_TIMEOUT)
        url = f"https://api.sofascore.com/api/v1/player/{id}"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()["player"]
        player_id = response_json["id"]
        first_name,last_name = response_json["name"].split(" ")
        jersey_number = response_json["jerseyNumber"]
        date_of_birth = response_json["dateOfBirthTimestamp"]
        position = response_json["position"]
        country = response_json["country"]["name"]
        team_id = response_json["team"]["id"]
        return Player(player_id, first_name,last_name,jersey_number,date_of_birth,position,country,team_id)


    def get_team_info(self,id):
        sleep(self.API_TIMEOUT)
        url = f"https://api.sofascore.com/api/v1/team/{id}"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()["team"]
        team_id = response_json["id"]
        name = response_json["name"]
        short_name = response_json["shortName"]
        namecode = response_json["nameCode"]
        stadium = response_json["venue"]["stadium"]["name"]
        return Team(team_id, name, short_name, namecode, stadium)
