import json
from games import Games
from enum import Enum
import data

# match_history = sorted(match_history, key=lambda x: x.get('startgametime', 0), reverse=True)

# tymczasowe, później do klasy z cohaczami
class Cohacze(Enum):
    Ing = 5850752
    Garneck = 3745878
    woyna = 3734845
    

# data.update_database_matches(Cohacze)
# data.update_database_profiles(Cohacze)

# data.update_database(Cohacze)

games = Games()
games.get_history_simplified()
games.sort_games()



# print(f"last_game: {Games.last_games}")

# with open("results.json", "w") as json_file:
#     json.dump(games.last_games, json_file, indent=4)















