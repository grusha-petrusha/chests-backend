from src import tools
from src import Game

def test_game_create_room():
    game_test1 = Game()
    id_test = game_test1.create_room({"name": "create_test1",
      "players_count": 4})
    
    
    assert game_test1.rooms[id_test].settings == {"name": "create_test1",
      "players_count": 4}
    
def test_game_join_room():
    game_test2 = Game()
    id_test_room = game_test2.create_room({"name": "create_test2",
      "players_count": 2})
    id_test, settings_test = game_test2.join_room({"room_id": id_test_room, "nickname": "A"})
    
    assert settings_test == {"name": "create_test2",
      "players_count": 2} and isinstance(id_test, str)
    
def test_game_join_room_with_same_nickname():
    game_test3 = Game()
    id_test_room = game_test3.create_room({"name": "create_test3",
      "players_count": 2})
    id_test, settings_test = game_test3.join_room({"room_id": id_test_room, "nickname": "A"})
    id_test2, settings_test2 = game_test3.join_room({"room_id": id_test_room, "nickname": "A"})

    assert id_test!=id_test and settings_test == settings_test2 and settings_test == {"name": "create_test3",
      "players_count": 2}
    
def test_game_get_state_room():
    game_test4 = Game()
    id_test_room = game_test4.create_room({"name": "create_test4",
      "players_count": 2})
    id_test, settings_test = game_test4.join_room({"room_id": id_test_room, "nickname": "A"})
    id_test2, settings_test2 = game_test4.join_room({"room_id": id_test_room, "nickname": "B"})
    result = game_test4.get_state({"player_id": id_test, "player_id": id_test2})
    
    assert result!=None and isinstance(result, tuple) and len(result)==3
    
def test_game_give_card():
    game_test5 = Game()
    id_test_room = game_test5.create_room({"name": "create_test5",
      "players_count": 2})
    id_test, settings_test = game_test5.join_room({"room_id": id_test_room, "nickname": "A"})
    id_test2, settings_test2 = game_test5.join_room({"room_id": id_test_room, "nickname": "B"})
    result = game_test5.give_card({"player_id": id_test,
      "nickname": "A",
      "card":1})
    
    assert result != None


    
    