import pytest
from game.game import Game

game = Game()

# article on testing functions with user input - https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
def test_game_setup(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "human")
    assert game.game_setup() == "human"
    
def test_game_setup(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "computer")
    assert game.game_setup() == "computer"
