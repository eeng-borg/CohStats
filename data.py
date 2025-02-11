import json
import requests
from datetime import datetime
import os
import time



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
        with open("data.json", "w") as json_file:
            json.dump(response_json, json_file, indent=4)  # `indent=4` makes it readable
        
        _request_duration(r_start)
        return response_json

    else:
        print("Error:", response.status_code)
        exit(1)





# lista się resetuje co cykl w funckji powyżej
def _filter_duplicates(new_list, list):

    for new_element in new_list:

        # for testing
        try:
            print(f"{new_element['id']} - {datetime.fromtimestamp(new_element["startgametime"])}")
        except:
            pass


        if not any(new_element['id'] == entry['id'] for entry in list):
            
            print(f"{new_element['id']} joined!!")
            print(', '.join(str(new_element['id']) for new_element in list))
            list.append(new_element)

   
    return list




def load_database_matches(file_name = "database_matches.json"):

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:

            cohacze_matches = json.load(f)
            return cohacze_matches
    
    else:
        return []
        


def _save_cohacze_matches_json(combine_matches, file_name = "databse_matches.json"):

    # write in file just for visualisation
    with open(file_name, "w") as json_file:

        json.dump(combine_matches, json_file, indent=4)  # `indent=4` makes it readable



# filter out and combine matches of serwer serwer players
def update_databse_matches(players, load_database_matches = load_database_matches, get_response = _get_response, filter_duplicates = _filter_duplicates):

    combine_matches = load_database_matches()

    # get history from each player
    for player in players:
        print(f"---------------\n {player.name}\n")

        match_history = get_response(player.value) # fetch player games history
        match_history_stats = match_history["matchHistoryStats"] # get games stats, there are also profiles of players and other stuff
        print(f"All games: {len(match_history_stats)}")

        # avoid duplicates, checks if match with given id is not already present in combine matches list
        combine_matches = filter_duplicates(match_history_stats, combine_matches)

    print(f"combine_matches: {len(combine_matches)}")
    print(', '.join(str(match['id']) for match in combine_matches))

    _save_cohacze_matches_json(combine_matches)
    return combine_matches





def get_profiles(players, get_response = _get_response):

    profiles = get_response(players)
    with open("profiles.json", "w") as f:
        json.dump(profiles, f)
        
    return list(profiles)




def update_database(players, update_databse_matches=update_databse_matches):

    # update
    update_databse_matches(players)
        


    
    
    



