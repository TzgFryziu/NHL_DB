from database_connection.nhl_db import NHL_DB

db = NHL_DB()

db.insert_matches()
db.insert_players_stats()



# for id in events.all_events_id[:1]:
#     match = events.get_match(id)
#     events.all_matches.append(match)

# for id in events.all_events_id[:1]:
#     stats = events.get_players_stats(id)
#     events.all_players_stats.extend(stats)
        


# for event in events.all_matches:
#     print(event)
# for event in events.all_players_stats:
#     print(event)

# print(events.get_player_info(898229))
# print(events.get_team_info(3687))





