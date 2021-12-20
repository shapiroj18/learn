# To Do: If board value is already filled in, don't allow


class Board:
    def __init__(self):
        self.possible_positions = [
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
        self.possible_values = ["X", "O"]

        # initialize board values into a dict with None values
        self.initial_board = {i: None for i in self.possible_positions}

        # get lists of keys in rows, columns and diagonals
        self.horizontals = [
            ["row_1_col_1", "row_1_col_2", "row_1_col_3"],
            ["row_2_col_1", "row_2_col_2", "row_2_col_3"],
            ["row_3_col_1", "row_3_col_2", "row_3_col_3"],
        ]

        self.verticals = [
            ["row_1_col_1", "row_2_col_1", "row_3_col_1"],
            ["row_1_col_2", "row_2_col_2", "row_3_col_2"],
            ["row_1_col_3", "row_2_col_3", "row_3_col_3"],
        ]

        self.diagonals = [
            ["row_1_col_1", "row_2_col_2", "row_3_col_3"],
            ["row_1_col_3", "row_2_col_2", "row_3_col_1"],
        ]

    def fill_board_value(self, board: dict, position: str, value: str) -> dict:
        """
        Fills new value into board
        """
        if position not in self.possible_positions:
            raise ValueError("Invalid board position")

        if value not in self.possible_values:
            raise ValueError("Invalid board value")

        board[position] = value

        return board

    def determine_game_end(self, board: dict) -> list:

        # check if horizontals are filled with all of the same value
        for i in self.horizontals:
            vals = []
            for j in i:
                vals.append(board[j])

            if None not in vals and len(set(vals)) == 1:
                return i

        # check if verticals are filled with all of the same value
        for i in self.verticals:
            vals = []
            for j in i:
                vals.append(board[j])

            if None not in vals and len(set(vals)) == 1:
                return i

        # check if diagonals are filled with all of the same value
        for i in self.diagonals:
            vals = []
            for j in i:
                vals.append(board[j])

            if None not in vals and len(set(vals)) == 1:
                return i

        # check if all values in board are filled in
        if all(i for i in board.values()):
            return [i for i in board.keys()]

        else:
            return False

    def _render_value(self, value):
        return value if value is not None else "-"

    # board style from https://betterprogramming.pub/tic-tac-toe-with-python-8fb6d666b13f
    def render_board(self, board: dict) -> str:

        return f"""
        1     2     3
     ___________________
     |     |     |     |
  1  |  {self._render_value(board['row_1_col_1'])}  |  {self._render_value(board['row_1_col_2'])}  |  {self._render_value(board['row_1_col_3'])}  |
     |     |     |     |
     |-----------------|
     |     |     |     |
  2  |  {self._render_value(board['row_2_col_1'])}  |  {self._render_value(board['row_2_col_2'])}  |  {self._render_value(board['row_2_col_3'])}  |
     |     |     |     |
     |-----------------|
     |     |     |     |
  3  |  {self._render_value(board['row_3_col_1'])}  |  {self._render_value(board['row_3_col_2'])}  |  {self._render_value(board['row_3_col_3'])}  |
     |     |     |     |
     |-----------------|
    """
