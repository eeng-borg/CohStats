from unittest import result
import pytest
from data import _filter_duplicates, load_database_matches
from data import _filter_duplicates
from unittest.mock import patch, MagicMock
import data
import json
import os
from data import update_database_matches, update_database_profiles, update_database


class TestFilterDuplicates:

    def test__no_duplicates(self):
        
        combined_matches = []
        matches_list = [
            {'id': 1},
            {'id': 2},
            {'id': 3}
        ]

        result = _filter_duplicates(matches_list, combined_matches, 'id')
        assert len(result) == 3
        assert result == matches_list



    def test__with_duplicates(self):

        combined_matches = []

        matches_list = [
            {'id': 1, 'description': 'match1'},
            {'id': 2, 'description': 'match2'},
            {'id': 1, 'description': 'match1_duplicate'},
            {'id': 3, 'description': 'match3'},
            {'id': 2, 'description': 'match2_duplicate'}
        ]

        result = _filter_duplicates(matches_list, combined_matches, 'id')

        assert len(result) == 3
        assert {'id': 1, 'description': 'match1'} in result
        assert {'id': 2, 'description': 'match2'} in result
        assert {'id': 3, 'description': 'match3'} in result


    def test__empty_list(self):
        combined_matches = []
        matches_list = []
        result = _filter_duplicates(matches_list, combined_matches, 'id')
        assert len(result) == 0
        assert result == []



    def test__all_duplicates(self):

        combined_matches = []
        matches_list = [
            {'id': 1, 'description': 'match1'},
            {'id': 1, 'description': 'match1_duplicate'},
            {'id': 1, 'description': 'match1_duplicate2'}
        ]

        result = _filter_duplicates(matches_list, combined_matches, 'id')
        assert len(result) == 1
        assert {'id': 1, 'description': 'match1'} in result




# class TestFilterCustoms:

#     def test_no_customs(self):
#         matches_list = [
#             {'id': 1, 'description': 'AUTOMATCH'},
#             {'id': 2, 'description': 'AUTOMATCH'},
#             {'id': 3, 'description': 'AUTOMATCH'}
#         ]

#         result = _filter_customs(matches_list)
#         assert len(result) == 0
#         assert result == []


#     def test_with_customs(self):
#         matches_list = [
#             {'id': 1, 'description': 'SESSION_MATCH_KEY'},
#             {'id': 2, 'description': 'AUTOMATCH'},
#             {'id': 3, 'description': 'SESSION_MATCH_KEY'}
#         ]

#         result = _filter_customs(matches_list)
#         assert len(result) == 2
#         assert {'id': 1, 'description': 'SESSION_MATCH_KEY'} in result
#         assert {'id': 3, 'description': 'SESSION_MATCH_KEY'} in result


#     def test_empty_list(self):
#         matches_list = []
#         result = _filter_customs(matches_list)
#         assert len(result) == 0
#         assert result == []


#     def test_all_customs(self):
#         matches_list = [
#             {'id': 1, 'description': 'SESSION_MATCH_KEY'},
#             {'id': 2, 'description': 'SESSION_MATCH_KEY'},
#             {'id': 3, 'description': 'SESSION_MATCH_KEY'}
#         ]

#         result = _filter_customs(matches_list)
#         assert len(result) == 3
#         assert result == matches_list



class TestUpdateDatabase:

    @staticmethod
    def dummny_get_response(arg):

        if arg == 1:
            return {
                "matchHistoryStats": [
                    {'id': 1, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 2, 'description': 'AUTOMATCH'},
                    {'id': 3, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 4, 'description': 'SESSION_MATCH_KEY'},
                    ],
                "profiles":[
                    {"profile_id": 1},
                    {"profile_id": 2},
                    {"profile_id": 3},
                    {"profile_id": 4},

                ]
            }
        
        elif arg == 2:
            return {
                "matchHistoryStats": [
                    {'id': 3, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 4, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 5, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 6, 'description': 'AUTOMATCH'}
                    ],
                "profiles": [
                    {"profile_id": 3},
                    {"profile_id": 4},
                    {"profile_id": 5},
                    {"profile_id": 6},
                    ]
                    
            }
        
        else:
            return {
                "matchHistoryStats": [],
                "profiles": []
            }



    
    @staticmethod
    def dummy_save_database(*args):
        pass 


    @pytest.fixture
    def players(self):
        return [MagicMock(value=1), MagicMock(value=2)]
    


    def test_update_matches_new(self, players):
     
        # Call the function
        result = update_database_matches(players, lambda: [], TestUpdateDatabase.dummy_save_database,  TestUpdateDatabase.dummny_get_response)

        # Assertions
        assert len(result) == 6
        assert {'id': 1, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 2, 'description': 'AUTOMATCH'} in result
        assert {'id': 3, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 4, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 5, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 6, 'description': 'AUTOMATCH'} in result

    # def existing_database



    def test_update_matches_on_existing(self, players):

        
        database = [
            {'id': 1, 'description': 'SESSION_MATCH_KEY'},
            {'id': 7, 'description': 'AUTOMATCH'}

        ]
        # Call the function
        result = update_database_matches(players, lambda: database, TestUpdateDatabase.dummy_save_database,  TestUpdateDatabase.dummny_get_response)

        # Assertions
        assert len(result) == 7
        assert {'id': 1, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 2, 'description': 'AUTOMATCH'} in result
        assert {'id': 3, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 4, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 5, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 6, 'description': 'AUTOMATCH'} in result
        assert {'id': 7, 'description': 'AUTOMATCH'} in result



    def test_update_profiles_new(self, players):

        result = update_database_profiles(players, lambda:[], TestUpdateDatabase.dummny_get_response, TestUpdateDatabase.dummy_save_database)
        assert len(result) == 6
        
        for id in range(6):
            assert {"profile_id": id + 1} in result



    def test_update_profiles_on_existing(self, players):

        result = update_database_profiles(players, lambda:[{"profile_id": 1}, {"profile_id": 7}], TestUpdateDatabase.dummny_get_response, TestUpdateDatabase.dummy_save_database)
        assert len(result) == 7
        
        for id in range(7):
            assert {"profile_id": id + 1} in result



    def test_update_database_new(self,players):


        result = update_database(players,
                                 load_database_matches=lambda:[],
                                 load_database_profiles=lambda:[],
                                 get_response=TestUpdateDatabase.dummny_get_response, 
                                 save_database=TestUpdateDatabase.dummy_save_database)
        
        assert len(result) == 2



    def test_update_database_on_existing(self,players):

        old_database_matches = [
            {'id': 1, 'description': 'SESSION_MATCH_KEY'},
            {'id': 7, 'description': 'AUTOMATCH'}

        ]
        old_database_profiles = [{"profile_id": 1}, {"profile_id": 7}]

        result = update_database(players,
                                 load_database_matches=lambda:old_database_matches,
                                 load_database_profiles=lambda:old_database_profiles,
                                 get_response=TestUpdateDatabase.dummny_get_response, 
                                 save_database=TestUpdateDatabase.dummy_save_database)
        
        assert len(result) == 2




class TestLoadCohaczeMatchesJson:


    @staticmethod
    def dummy_os_path_exists_true(*args):
        return True
    


    @staticmethod
    def dummy_os_path_exists_false(*args):
        return False
    


    @pytest.fixture
    def test_file(self):

        with open("test.json", "w") as json_file:

            json.dump([], json_file, indent=4)
        
    

    # def test__file_exists(self, monkeypatch, tmp_path):
    #     monkeypatch.setattr(os.path, "exists", TestLoadCohaczeMatchesJson.dummy_os_path_exists_true)

    #     file_path  = tmp_path / "test.json"
    #     file_content = [{'id': 1}, {'id': 2}]
    #     file_path.write_text(json.dumps(file_content))

    #     result = data._load_cohacze_matches_json('test.json')
    #     assert len(result) == 2
    #     assert {'id': 1} in result
    #     assert {'id': 2} in result


    def test_file_not_exists(self):

        result = data.load_database_matches('test.json')
        assert result == []



