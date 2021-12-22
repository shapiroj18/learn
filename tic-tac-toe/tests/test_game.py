import pytest
from game.game import Game
from game.board import Board

game = Game()
board = Board()

# article on testing functions with user input - https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
def test_game_setup(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "human")
    assert game.game_setup() == "human"


def test_game_setup(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "computer")
    assert game.game_setup() == "computer"


def test_get_names(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Jonathan")
    assert game.get_names("computer") == ("Jonathan", "computer")


def test_get_elements(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "x")
    assert game.get_elements("j", "k", "human") == ("X", "O")


def test_get_elements(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "x")
    assert game.get_elements("j", "computer", "computer") == ("X", "O")


def test_make_move(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "1,3")

    assert game.make_move(
        current_board={
            "row_1_col_1": "X",
            "row_1_col_2": "X",
            "row_1_col_3": None,
            "row_2_col_1": "O",
            "row_2_col_2": "O",
            "row_2_col_3": None,
            "row_3_col_1": None,
            "row_3_col_2": None,
            "row_3_col_3": None,
        },
        player="j",
        element="X",
    ) == {
        "row_1_col_1": "X",
        "row_1_col_2": "X",
        "row_1_col_3": "X",
        "row_2_col_1": "O",
        "row_2_col_2": "O",
        "row_2_col_3": None,
        "row_3_col_1": None,
        "row_3_col_2": None,
        "row_3_col_3": None,
    }
