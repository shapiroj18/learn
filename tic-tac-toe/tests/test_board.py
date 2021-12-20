import pytest
from game.board import Board

board = Board()


def test_init():
    assert board.possible_positions == [
        "row_1_col_1",
        "row_1_col_2",
        "row_1_col_3",
        "row_2_col_1",
        "row_2_col_2",
        "row_2_col_3",
        "row_3_col_1",
        "row_3_col_2",
        "row_3_col_3",
    ]


def test_possible_values():
    assert board.possible_values == ["X", "O"]


def test_initial_board():
    assert board.initial_board == {
        "row_1_col_1": None,
        "row_1_col_2": None,
        "row_1_col_3": None,
        "row_2_col_1": None,
        "row_2_col_2": None,
        "row_2_col_3": None,
        "row_3_col_1": None,
        "row_3_col_2": None,
        "row_3_col_3": None,
    }


def test_horizontals():
    assert board.horizontals == [
        ["row_1_col_1", "row_1_col_2", "row_1_col_3"],
        ["row_2_col_1", "row_2_col_2", "row_2_col_3"],
        ["row_3_col_1", "row_3_col_2", "row_3_col_3"],
    ]


def test_verticals():
    assert board.verticals == [
        ["row_1_col_1", "row_2_col_1", "row_3_col_1"],
        ["row_1_col_2", "row_2_col_2", "row_3_col_2"],
        ["row_1_col_3", "row_2_col_3", "row_3_col_3"],
    ]


def test_diagonals():
    assert board.diagonals == [
        ["row_1_col_1", "row_2_col_2", "row_3_col_3"],
        ["row_1_col_3", "row_2_col_2", "row_3_col_1"],
    ]


def test_fill_board_value():
    test_board = board.fill_board_value(board.initial_board, "row_1_col_1", "X")
    assert test_board["row_1_col_1"] == "X"


def test_fill_board_value_position_error():
    with pytest.raises(ValueError):
        board.fill_board_value(board.initial_board, "not_a_board_position", "X")


def test_fill_board_value_value_error():
    with pytest.raises(ValueError):
        board.fill_board_value(board.initial_board, "row_1_col_1", "invalid_value")


def test_determine_game_end_horizontal_true():
    test_board = {
        "row_1_col_1": "X",
        "row_1_col_2": "X",
        "row_1_col_3": "X",
        "row_2_col_1": None,
        "row_2_col_2": None,
        "row_2_col_3": None,
        "row_3_col_1": None,
        "row_3_col_2": None,
        "row_3_col_3": None,
    }
    assert board.determine_game_end(test_board) == [
        "row_1_col_1",
        "row_1_col_2",
        "row_1_col_3",
    ]


def test_determine_game_end_vertical_true():
    test_board = {
        "row_1_col_1": "X",
        "row_1_col_2": None,
        "row_1_col_3": None,
        "row_2_col_1": "X",
        "row_2_col_2": None,
        "row_2_col_3": None,
        "row_3_col_1": "X",
        "row_3_col_2": None,
        "row_3_col_3": None,
    }
    assert board.determine_game_end(test_board) == [
        "row_1_col_1",
        "row_2_col_1",
        "row_3_col_1",
    ]


def test_determine_game_end_diagonal_true():
    test_board = {
        "row_1_col_1": "X",
        "row_1_col_2": None,
        "row_1_col_3": None,
        "row_2_col_1": None,
        "row_2_col_2": "X",
        "row_2_col_3": None,
        "row_3_col_1": None,
        "row_3_col_2": None,
        "row_3_col_3": "X",
    }
    assert board.determine_game_end(test_board) == [
        "row_1_col_1",
        "row_2_col_2",
        "row_3_col_3",
    ]


def test_determine_game_end_full_true():
    test_board = {
        "row_1_col_1": "X",
        "row_1_col_2": "O",
        "row_1_col_3": "X",
        "row_2_col_1": "O",
        "row_2_col_2": "X",
        "row_2_col_3": "O",
        "row_3_col_1": "O",
        "row_3_col_2": "X",
        "row_3_col_3": "O",
    }
    assert board.determine_game_end(test_board) == [
        "row_1_col_1",
        "row_1_col_2",
        "row_1_col_3",
        "row_2_col_1",
        "row_2_col_2",
        "row_2_col_3",
        "row_3_col_1",
        "row_3_col_2",
        "row_3_col_3",
    ]


def test_determine_game_end_full_false():
    test_board = {
        "row_1_col_1": "X",
        "row_1_col_2": None,
        "row_1_col_3": None,
        "row_2_col_1": None,
        "row_2_col_2": None,
        "row_2_col_3": None,
        "row_3_col_1": None,
        "row_3_col_2": None,
        "row_3_col_3": None,
    }
    assert board.determine_game_end(test_board) == False


def test_private_render_value():
    assert board._render_value(None) == "-"


def test_private_render_value():
    assert board._render_value("X") == "X"
