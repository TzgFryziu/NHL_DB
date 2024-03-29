import requests
import json
from time import sleep
from ..dataclasses_container.Match import Match

class Events:
    def __init__(self):
        self.API_TIMEOUT = 2
        self.api_headers_common = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        self.main_url = 'https://api.sofascore.com/api/v1/unique-tournament/234/season/52528/events/last/0'
        self.response = requests.get(self.main_url, headers=self.api_headers_common)
        self.all_events_id = [event["id"]for event in self.response.json()["events"]]
        self.all_matches = []
        for id in self.all_events_id:
            match = self.get_match(id)
            self.all_matches.append(match)
        
        
    def get_match(self, id):
        return Match(self.get_basic_info(id), self.get_odds(id))

    def get_basic_info(self,id):
        sleep(self.API_TIMEOUT)
        url = f"https://api.sofascore.com/api/v1/event/{id}"
        response = requests.get(url, headers=self.api_headers_common)
        response_json = response.json()
        match_id = response_json["id"]["event"]
        date = response_json["startTimestamp"]
        home_team = response_json["homeTeam"]["name"]
        away_team = response_json["awayTeam"]["name"]
        home_score = response_json["homeScore"]["current"]
        away_score = response_json["awayScore"]["current"]
        return (match_id, date, home_team, away_team, home_score, away_score)
    
    def get_odds(self,id):
        pass