import json
from games_list import GamesList
from enum import Enum
import data
from enums import Cohacze

# match_history = sorted(match_history, key=lambda x: x.get('startgametime', 0), reverse=True)

# tymczasowe, później do klasy z cohaczami
    

# data.update_database_matches(Cohacze)
# data.update_database_profiles(Cohacze)

# data.update_database(Cohacze)

games = GamesList()
games.get_history_simplified()
games.filter_games("mapname", filter_by="4p_einhoven_country")
games.sort_games(sort_by='start_timestamp')





# print(f"last_game: {GamesList.last_games}")

with open("results.json", "w") as json_file:
    json.dump(games.last_games_filtered, json_file, indent=4)















