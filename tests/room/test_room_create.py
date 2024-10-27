from src import tools
from .room_fixtures import *


def test_room_create_with_many_players():
  room_data = room.Room({
    "name": "room with a lot of players",
    "players_count": 10000000000 
  })

  assert tools.validate(room_data.settings, {
    "error_code": int,
    "room_id": str
  }) == False


def test_room_create_with_long_name():
  room_data = room.Room({
    "name": "a"*100,
    "players_count": 1
  })

  assert tools.validate(room_data.settings, {
    "error_code": int,
    "room_id": str
  }) == False
  

def test_room_create_with_zero_name():
  room_data = room.Room({
    "name": "",
    "players_count": 1
  })

  assert tools.validate(room_data.settings, {
    "error_code": int,
    "room_id": str
  }) == False


def test_room_create_with_zero_players():
  room_data = room.Room({
    "name": "room_with_zero_players",
    "players-count": 0
  })

  assert tools.validate(room_data.settings, {
    "error_code": int,
    "room_id": str
  }) == False
