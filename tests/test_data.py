import pytest
from data import _filter_duplicates
from data import _filter_duplicates
from unittest.mock import patch, MagicMock
import data
import json
import os
from data import update_databse_matches


class TestFilterDuplicates:

    def test__no_duplicates(self):
        
        combined_matches = []
        matches_list = [
            {'id': 1},
            {'id': 2},
            {'id': 3}
        ]

        result = _filter_duplicates(matches_list, combined_matches)
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

        result = _filter_duplicates(matches_list, combined_matches)

        assert len(result) == 3
        assert {'id': 1, 'description': 'match1'} in result
        assert {'id': 2, 'description': 'match2'} in result
        assert {'id': 3, 'description': 'match3'} in result


    def test__empty_list(self):
        combined_matches = []
        matches_list = []
        result = _filter_duplicates(matches_list, combined_matches)
        assert len(result) == 0
        assert result == []



    def test__all_duplicates(self):

        combined_matches = []
        matches_list = [
            {'id': 1, 'description': 'match1'},
            {'id': 1, 'description': 'match1_duplicate'},
            {'id': 1, 'description': 'match1_duplicate2'}
        ]

        result = _filter_duplicates(matches_list, combined_matches)
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



class TestGetCohaczeMatches:

    @staticmethod
    def dummny_get_response(arg):

        if arg == 1:
            return {
                "matchHistoryStats": [
                    {'id': 1, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 2, 'description': 'AUTOMATCH'},
                    {'id': 3, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 6, 'description': 'SESSION_MATCH_KEY'},
                    ]
            } 
        
        if arg == 2:
            return {
                "matchHistoryStats": [
                    {'id': 3, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 6, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 9, 'description': 'SESSION_MATCH_KEY'},
                    {'id': 13, 'description': 'AUTOMATCH'}
                    ]
            }     


    
    @staticmethod
    def dummny_save_cohacze_matches_json(*args):
        pass 



    def test_get_our_matches(self, monkeypatch):

        # Mock cohacze enums
        players = [MagicMock(value=1), MagicMock(value=2)]
        
        monkeypatch.setattr(data, "_save_cohacze_matches_json", TestGetCohaczeMatches.dummny_save_cohacze_matches_json)

        # Call the function
        result = update_databse_matches(players, lambda: [], TestGetCohaczeMatches.dummny_get_response)

        # Assertions
        assert len(result) == 6
        assert {'id': 1, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 2, 'description': 'AUTOMATCH'} in result
        assert {'id': 3, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 6, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 9, 'description': 'SESSION_MATCH_KEY'} in result
        assert {'id': 13, 'description': 'AUTOMATCH'} in result




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



