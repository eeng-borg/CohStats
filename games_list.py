from data import load_database_matches, load_database_profiles, update_database
import math
from datetime import datetime
from enums import Cohacze, DatabaseType, Factions


class GamesList:

    # instance injection for easier testing,
    def __init__(self, load_database_matches = load_database_matches, load_database_profiles = load_database_profiles, update_database = update_database):

        self.load_database_matches = load_database_matches
        self.load_database_profiles = load_database_profiles
        self.update_database = update_database

        # use it as a base for filtering games, updated by get_history_simplified
        self._last_games = []

        # games to display, even if no filtering is aplied
        self.last_games_filtered = []

        # saved options - when database id updated, it return to default sorting order and filtering (random order and no filter)
        # When sorting func or filtering is called, we save their arguments.
        # So when database is updated, we can call those functions with saved arguments, to return our list
        # to the state it was before database update

        self.saved__sort_by = 1739617010
        self.saved__reversed = True

        self.saved__filter_category = None
        self.saved__filter_sub_category = None
        self.saved__filter_by = None




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



    # # return players from on of the team, get their names and faction
    # def _get_players(self, match, team, get_player_name = None, race_id_to_name = _race_id_to_name):

    #     print(f"get players")
    #     players_list = match['matchhistoryreportresults']
    #     players_in_team = []

    #     for player in players_list:
    #         if player['teamid'] == team:

    #             player_dict = {}

    #             if get_player_name is None:
    #                 player_dict['name'] = self._get_player_name(player['profile_id']) # convert id to name

    #             player_dict['faction'] = race_id_to_name(player['race_id']) # convert id to name
    #             players_in_team.append(player_dict)
        

    #     return players_in_team
    @staticmethod
    def _sort_players_by_team(players):

        sorted_team = sorted(players, key=lambda x: x['team'])
        return sorted_team
    

    
    # return players from on of the team, get their names and faction
    def _get_players(self, match, get_player_name=None, race_id_to_name=_race_id_to_name, sort_players_by_team=_sort_players_by_team):

        print(f"get players")
        players_list = match['matchhistoryreportresults']
        players_in_team = []

        for player in players_list:
            player_dict = {}

            if get_player_name is None:
                player_dict['name'] = self._get_player_name(player['profile_id']) # convert id to name

            player_dict['faction'] = race_id_to_name(player['race_id']) # convert id to name
            player_dict['team'] = player['teamid']

            players_in_team.append(player_dict)
        

        return sort_players_by_team(players_in_team)
    



    @staticmethod
    def _get_match_type(description):

        if description == "AUTOMATCH":
            return "Automatch"
        
        else:
            return "Custom"




    @staticmethod
    def _get_match_result(match):

        player_results = match["matchhistoryreportresults"]
        
        for player in player_results:

            # look for the first player who won in that game (1 - won, 0 - lost) and then check his team
            if player["resulttype"] == 1:

                winning_team = player["teamid"]
                return winning_team





    # get data from database and create a simplified and easy to read version of game statistics
    def get_history_simplified(self, get_game_format = _get_game_format, convert_time = _convert_time, get_game_duration = _get_game_duration, get_players = None, get_match_type = _get_match_type, do_update_databse=True, get_match_result=_get_match_result):


        if do_update_databse == True:
            self.update_database()
        
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
            simplified_match_stat['winner_team'] = get_match_result(match)

            if get_players is None:
                simplified_match_stat['players'] = self._get_players(match)



            self._last_games.append(simplified_match_stat)
            

        # print(f"Game stats: {self._last_games}")

        #
        self.last_games_filtered = self._last_games
        # print(f"self._last_games: {self._last_games}")
        return self._last_games
    
    


    def sort_games(self, last_games_filtered=None, sort_by=None, reverse=True):

        if sort_by == None:
            sort_by = self.saved__sort_by#'start_timestamp'

        else: 
            self.saved__sort_by = sort_by



        print('sorting started')
        # Use self._last_games if no argument is provided
        if last_games_filtered is None:
            last_games_filtered = self.last_games_filtered
        

        self.last_games_filtered = sorted(last_games_filtered, key=lambda x: x.get(sort_by, 0), reverse=reverse)

        # print("----------\n Sorted")
        # print([game[sort_by] for game in self.last_games_filtered])


        return self.last_games_filtered
    




    # filter sub category for filtering nested keys
    def filter_games(self, last_games_to_filter=None, filter_category=None, filter_sub_category=None, filter_by=None):
        
        # setting default or saved options for filtering - if no arguments are give
        # if args are given - save them, to use later
        if filter_category==None:
            filter_category = self.saved__filter_category
        else:
            self.saved__filter_category = filter_category


        if filter_sub_category==None:
            filter_sub_category = self.saved__filter_sub_category
        else:
            self.saved__filter_sub_category = filter_sub_category


        if filter_by==None:
            filter_by = self.saved__filter_by
        else:
            self.saved__filter_by = filter_by

    



        self.last_games_filtered = []


        for game in self._last_games:
            
            if filter_sub_category == None:
                
                # if no filter category is provided, then do not perform filtering and return all games
                if filter_category != None:

                    if game[filter_category] == filter_by:
                        self.last_games_filtered.append(game)
                

                else:
                    self.last_games_filtered = list(self._last_games)
                

            else:
                if game[filter_category][filter_sub_category] == filter_by:
                    self.last_games_filtered.append(game)
        

        return self.last_games_filtered




