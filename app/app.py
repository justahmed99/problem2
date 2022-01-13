from flask import Flask
from flask import request, jsonify
from flask.helpers import make_response
from flask_swagger_ui import get_swaggerui_blueprint

# App Configs
app = Flask(__name__)
app.config["DEBUG"] = True

#Swagger Configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Soccer API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


teams = []
players = []

@app.post("/teams")
def teams_add() :
    req = request.get_json()
    team_name = req["name"]

    if team_name in teams :
        return make_response(
            jsonify(response = {
                "message": "Team already exist!",
                "status": False
            }), 403
        )

    teams.append(team_name)

    return make_response(
        jsonify(response = {
            "message": "Team added",
            "status": True
        }), 201
    )

@app.get("/teams")
def teams_get() :
    team_name = request.args.get("name")
    if team_name not in teams :
        return make_response(
            jsonify(response = {
                "message": "Team doesn't exist!",
                "status": False
            }), 404
        )
    
    team = [team for team in teams if team == team_name][0]
    
    list_players = [player for player in players if player["team"] == team]

    return make_response(
        jsonify(response = {
            "message": "Get team",
            "data": {
                "team": team,
                "players": list_players
            },
            "status": True
        }), 200
    )

@app.post("/players")
def players_add() :
    req = request.get_json()
    player_name = req["name"]
    player_number = req["number"]
    team_name = req["team_name"]
    if not any(team == team_name for team in teams) :
        return make_response(
            jsonify(response = {
                "message": "Team doesn't exist!",
                "status": False
            }), 404
        )
    
    team = [team for team in teams if team == team_name][0]


    if any(ply["number"] == player_number and ply["team"] == team for ply in players) :
        return make_response(
            jsonify(response = {
                "message": f"Player with number {player_number} already exist in this team!",
                "status": False
            }), 403
        )

    player = {
        "name": player_name,
        "number": player_number,
        "team": team
    }

    players.append(player)

    return make_response(
        jsonify(response = {
            "message": "Player added",
            "status": True
        }), 201
    )

@app.get("/players")
def get_player():
    number = request.args.get("number")
    team_name = request.args.get("team")
    
    if not any(team == team_name for team in teams) : 
        return make_response(
            jsonify(response = {
                "message": "Team doesn't exist!",
                "status": False
            }), 404
        )
    
    team = [team for team in teams if team == team_name][0]

    if not any(player["number"] == int(number) and player["team"] == team for player in players) :
        return make_response(
            jsonify(response = {
                "message": "Player doesn't exist!",
                "status": False
            }), 404
        )

    player = [player for player in players if player["number"] == int(number) and player["team"] == team][0]
    return make_response(
        jsonify(response = {
            "message": "Player exist",
            "status": True,
            "data": {
                "name": player["name"],
                "number": player["number"],
                "team": player["team"]
            }
        }), 200
    )


if __name__ == "__main__" :
    app.run()