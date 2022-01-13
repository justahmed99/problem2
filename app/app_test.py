import unittest
import requests

API_URL = "http://localhost:5000/"

class ApiTest(unittest.TestCase) :

    # Create a new team
    def test_1_add_team(self) :
        url = f"{API_URL}teams"
        req_body = {
            "name": "Persija Jakarta"
        }

        req = requests.post(url, json=req_body)
        self.assertEqual(req.status_code, 201)

    # Avoid creating a same team twice
    def test_2_add_team_avoid_redundant(self) :
        url = f"{API_URL}teams"
        req_body = {
            "name": "Persija Jakarta"
        }

        req = requests.post(url, json=req_body)
        self.assertNotEqual(req.status_code, 201)

    # Search for a team that exist
    def test_3_get_team(self):
        url = f"{API_URL}teams?name=Persija Jakarta"
        req = requests.get(url)
        self.assertEqual(req.status_code, 200)

    # Search for a team that doesn't exist
    def test_4_get_team_not_exist(self):
        url = f"{API_URL}teams?name=Bali United"
        req = requests.get(url)
        self.assertEqual(req.status_code, 404)

    # Create new player
    def test_5_add_players(self):
        url = f"{API_URL}players"
        req_body = {
            "name": "Ismet Sofyan",
            "number": 14,
            "team_name": "Persija Jakarta"
        }

        req = requests.post(url, json=req_body)
        self.assertEqual(req.status_code, 201)

    # Create new other player
    def test_6_add_players_other(self):
        url = f"{API_URL}players"
        req_body = {
            "name": "Ahmad Bustomi",
            "number": 16,
            "team_name": "Persija Jakarta"
        }

        req = requests.post(url, json=req_body)
        self.assertEqual(req.status_code, 201)

    # Avoid creating player with same number
    def test_7_add_players_avoid_redundant(self):
        url = f"{API_URL}players"
        req_body = {
            "name": "Ismet Sofyan",
            "number": 14,
            "team_name": "Persija Jakarta"
        }

        req = requests.post(url, json=req_body)
        self.assertNotEqual(req.status_code, 201)
    
    # Searching for player that exist
    def test_7_search_for_player(self):
        number = "14"
        team = "Persija Jakarta"
        url = f"{API_URL}players?number={number}&team={team}"

        req = requests.get(url)
        self.assertEqual(req.status_code, 200)

    # Searching for player that doesn't exist
    def test_7_search_for_player(self):
        number = "20"
        team = "Persija Jakarta"
        url = f"{API_URL}players?number={number}&team={team}"

        req = requests.get(url)
        self.assertNotEqual(req.status_code, 200)