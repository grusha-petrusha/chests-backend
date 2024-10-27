from src import tools
from .api_fixtures import *


def test_api_give_ok(client, join_data_2):
  states_data = []
  for i in range(2):
    state_data = client.post("/api/getState", json={
      "player_id": join_data_2[i]["player_id"]
    }).json
    states_data.append(state_data)

  for i, state_data in enumerate(states_data):
    if state_data["turn"] == True:
      give_data = client.post("/api/giveCard", json={
        "player_id": join_data_2[i]["player_id"],
        "nickname": "Player_1" if i != 0 else "Player_2",
        "card": 0
      }).json

      assert tools.validate(give_data, {
        "error_code": int,
        "status": bool
      })

def test_api_give_to_not_exist_player(client, join_data_2):
  states_data = []
  for i in range(2):
    state_data = client.post("/api/getState", json={
      "player_id": join_data_2[i]["player_id"]
    }).json
    states_data.append(state_data)

  #print(states_data)
  #assert False
  for i, state_data in enumerate(states_data):
    if state_data["turn"] == True:
      give_data = client.post("/api/giveCard", json={
        "player_id": join_data_2[i]["player_id"],
        "nickname": "Player_3",
        "card": 0
      }).json
      
      print(give_data)
      assert tools.validate(give_data, {
        "error_code": int,
        "status": bool
      })