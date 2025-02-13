from data import load_database_matches, load_database_profiles
import math
from datetime import datetime
from enums import DatabaseType, Factions


class Games:

    # instance injection for easier testing,
    def __init__(self, load_database_matches = load_database_matches, load_database_profiles = load_database_profiles):

        self.load_database_matches = load_database_matches
        self.load_database_profiles = load_database_profiles
        self.last_games = []


    @staticmethod
    def _convert_time(match):
        
        start_timestamp = match["startgametime"]
        date_time = datetime.utcfromtimestamp(start_timestamp)
        # formated_date_time = date_time.strftime('%H:%M:%S %Y-%m-%d')

        return  {
            'year': date_time.year,
            'month': date_time.month,
            'day': date_time.day,
            'hour': date_time.hour,
            'minute': date_time.minute, 
            }


    @staticmethod
    def _get_game_duration(match, format):

        duration_timestamp = match['completiontime'] - match['startgametime']
        if format == 'timestamp':
            return duration_timestamp
        
        else:
            print(f'timestamp_dur: {duration_timestamp}')
            duration = datetime.utcfromtimestamp(duration_timestamp)

            return {
                "hours": duration.hour,
                "minutes": duration.minute
            }
        
    
    @staticmethod
    def _get_game_format(match):

        number_of_players = len(match["matchhistoryreportresults"])
        format = number_of_players/2
        return math.ceil(format)
    


    # data.profile
    
    def _get_player_name(self, player_id):

        print(f"player_id: {player_id}")


        for player_profile in self.load_database_profiles():

            if player_profile["profile_id"] == player_id:
                
                return player_profile["alias"]
        
        return None
    


    @staticmethod
    def _race_id_to_name(race_id):

        for faction in Factions:
            if faction.value == race_id:
                return str(faction.name)



    # return players from on of the team, get their names and faction
    def _get_players(self, match, team, get_player_name = None, race_id_to_name = _race_id_to_name):

        print(f"get players")
        players_list = match['matchhistoryreportresults']
        players_in_team = []

        for player in players_list:
            if player['teamid'] == team:

                player_dict = {}

                if get_player_name is None:
                    player_dict['name'] = self._get_player_name(player['profile_id']) # convert id to name

                player_dict['faction'] = race_id_to_name(player['race_id']) # convert id to name
                players_in_team.append(player_dict)
        

        return players_in_team
    

    @staticmethod
    def _get_match_type(description):

        if description == "AUTOMATCH":
            return "Automatch"
        
        else:
            return "Custom"





    # add to the existsing list, not reasing
    def get_history_simplified(self, get_game_format = _get_game_format, convert_time = _convert_time, get_game_duration = _get_game_duration, get_players = None, get_match_type = _get_match_type):

        cohacze_matches = self.load_database_matches()


        for match in cohacze_matches:

            simplified_match_stat = {}
            
            simplified_match_stat['id'] = match['id'] 
            simplified_match_stat['mapname'] = match['mapname']            
            simplified_match_stat['gameformat'] = get_game_format(match)
            simplified_match_stat['gametype'] = get_match_type(match['description'])
            simplified_match_stat['startgametime'] = convert_time(match)
            print(f"{simplified_match_stat['startgametime']} - {match['id']}")
            simplified_match_stat['start_timestamp'] = match['startgametime']
            simplified_match_stat['gameduration'] = get_game_duration(match, 'datetime')
            simplified_match_stat['duration_timestamp'] = get_game_duration(match, 'timestamp')

            if get_players == None:
                simplified_match_stat['team_0'] = self._get_players(match, team=0)
                simplified_match_stat['team_1'] = self._get_players(match, team=1)


            self.last_games.append(simplified_match_stat)
            

        # print(f"Game stats: {self.last_games}")

        return self.last_games
    
    

    def sort_games(self, games=None, sort_by = 'start_timestamp', reverse=True):

        print('sorting started')
        # Use self.last_games if no argument is provided
        if games is None:
            games = self.last_games
        
        self.last_games = sorted(games, key=lambda x: x.get(sort_by, 0), reverse=reverse)
        print("----------\n Sorted")
        print([game[sort_by] for game in self.last_games])


        return self.last_games