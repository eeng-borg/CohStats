import json
from multiprocessing.reduction import duplicate
import requests
from datetime import datetime
import os
import time

from enums import Cohacze, DatabaseType



def _request_duration(r_start):

    r_end = time.time() - r_start
    request_duration = datetime.utcfromtimestamp(r_end)
    print(f"Request completed in {request_duration.minute} minutes and {request_duration.second} seconds and {request_duration.microsecond} milis")



def _get_response(player_id):

    r_start = time.time()
    print(f"--------------\n Requesting: {player_id}")


    relic_id = player_id
    url = f"https://coh2-api.reliclink.com/community/leaderboard/getRecentMatchHistoryByProfileId?title=coh2&profile_id={relic_id}"
    response = requests.get(url)


    if response.status_code == 200:
        response_json = response.json()

        # write in file just for visualisation
        with open("data.json", "w", encoding='utf-8') as json_file:
            json.dump(response_json, json_file, indent=4)  # `indent=4` makes it readable
        
        _request_duration(r_start)
        
        return response_json

    else:
        print("Error:", response.status_code)
        exit(1)





# lista się resetuje co cykl w funckji powyżej
def _filter_duplicates(new_list, list, duplicate_key): # duplicate_key what value should we compare

    for new_element in new_list:

        # # for testing
        # try:
        #     print(f"{new_element[duplicate_key]} - {datetime.fromtimestamp(new_element["startgametime"])}")
        # except:
        #     pass


        if not any(new_element[duplicate_key] == entry[duplicate_key] for entry in list):
            
            # print(f"{new_element[duplicate_key]} joined!!")
            # print(', '.join(str(new_element[duplicate_key]) for new_element in list))
            list.append(new_element)

   
    return list




def load_database_matches(file_name = "database_matches.json"):

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:

            cohacze_matches = json.load(f)
            return cohacze_matches
    
    else:
        return []
        


def _save_database(database, database_type):

    file_name = f"database_{database_type}.json"
    # write in file just for visualisation
    with open(file_name, "w", encoding='utf-8') as json_file:

        json.dump(database, json_file, indent=4)  # `indent=4` makes it readable



def update_database_matches(players=Cohacze, load_database_matches=load_database_matches, save_database=_save_database, get_response=_get_response, filter_duplicates=_filter_duplicates) -> list:

    combine_matches = load_database_matches()

    # get history from each player
    for player in players:
        print(f"---------------\n {player.name}\n")

        match_history = get_response(player.value) # fetch player games history

        match_history_stats = match_history["matchHistoryStats"] # get games stats, there are also profiles of players and other stuff
        
        print(f"All games: {len(match_history_stats)}")

        # avoid duplicates, checks if match with given id is not already present in combine matches list
        combine_matches = filter_duplicates(match_history_stats, combine_matches, duplicate_key = 'id')

    print(f"combine_matches: {len(combine_matches)}")
    print(', '.join(str(match['id']) for match in combine_matches))

    save_database(combine_matches, DatabaseType.matches.value)

    return combine_matches



def load_database_profiles(file_name = "database_profiles.json"):

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:

            profiles = json.load(f)
            return profiles
    
    else:
        return []
    


def update_database_profiles(players = Cohacze, load_database_profiles = load_database_profiles, get_response = _get_response, save_database = _save_database, filter_duplicates = _filter_duplicates) -> list:

    combine_profiles = load_database_profiles()

    for player in players:

        database = get_response(player.value)
        new_profiles = database["profiles"]
        combine_profiles = filter_duplicates(new_profiles, combine_profiles, duplicate_key = 'profile_id')

    save_database(combine_profiles, DatabaseType.profiles.value)
        
    return combine_profiles



# update profiles and matches in the same time 
def update_database(
        players = Cohacze,
        update_databse_matches = update_database_matches, 
        update_database_profiles = update_database_profiles, 
        get_response = _get_response,
        load_database_profiles = load_database_profiles,
        load_database_matches = load_database_matches,
        save_database = _save_database
        ):

    # update
    database_matches = update_databse_matches(players, get_response=get_response, save_database=save_database, load_database_matches=load_database_matches)
    database_profiles = update_database_profiles(players, get_response=get_response, save_database=save_database, load_database_profiles=load_database_profiles)
    
    # mostly for testing
    return {"matches": database_matches, "profiles": database_profiles}

    
    
    



