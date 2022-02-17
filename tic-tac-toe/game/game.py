import sys
import re
from board import Board

# have  a quit function
# have an instructions function, including making moves


class Game:
    def __init__(self):
        ...

    def game_setup(self) -> str:
        player_2_type = (
            input("Do you want to play against another human or the computer? ")
            .strip()
            .lower()
        )
        accepted_values = ["human", "computer"]
        while player_2_type not in accepted_values:
            player_2_type = (
                input('You can only answer "human" or "computer": ').strip().lower()
            )

        return player_2_type

    def get_names(self, player_2_type: str) -> str:
        if player_2_type == "human":
            player_1_name = input("What is player 1's name?\n")
            player_2_name = input("What is player 2's name?\n")
            return player_1_name, player_2_name
        else:
            player_1_name = input("What is player 1's name?\n")
            return player_1_name, player_2_type

    def get_elements(
        self, player_1_name: str, player_2_name: str, player_2_type: str
    ) -> str:

        accepted_values = ["X", "O"]
        player_1_element = (
            input(f"Will {player_1_name} be X's or O's? ").strip().upper()
        )
        while player_1_element.strip().upper() not in accepted_values:
            player_1_element = input('You can only select "X" or "O" ').strip().upper()

        accepted_value_element = accepted_values.index(player_1_element)
        player_2_element = (
            accepted_values[0] if accepted_value_element == 1 else accepted_values[1]
        )

        if player_2_type == "human":
            print(
                f"\nGreat! {player_1_name} will be {player_1_element}'s and {player_2_name} will be {player_2_element}'s."
            )
            return player_1_element, player_2_element
        else:
            print(
                f"\nGreat! {player_1_name} will be {player_1_element}'s and the computer will be {player_2_element}'s."
            )
            return player_1_element, player_2_element

    def _moves_dict(self) -> dict:
        return {
            "1,1": "row_1_col_1",
            "1,2": "row_1_col_2",
            "1,3": "row_1_col_3",
            "2,1": "row_2_col_1",
            "2,2": "row_2_col_2",
            "2,3": "row_2_col_3",
            "3,1": "row_3_col_1",
            "3,2": "row_3_col_2",
            "3,3": "row_3_col_3",
        }

    def make_move(self, current_board: dict, player: str, element: str) -> dict:
        board = Board()
        print("Current board:")
        print(board.render_board(current_board))

        move = input(
            f'{player}\'s turn! Where would you like your next move to be?\nPlease enter in "row,column" format (rows increase top->bottom, columns increase left->right)\n\n'
        ).strip()
        
        pattern = re.compile("[1-3],[1-3]")
        possible_moves = self._moves_dict()
        while not pattern.fullmatch(move):
            move = input(
                'Your move must be in "row,column" format and contain numbers 1-3. For example, enter "3,1" for the bottom row and first column.\n'
            )

        while current_board[possible_moves[move]] is not None:
            move = input("That spot is taken, please select another.\n")

        new_board = board.fill_board_value(current_board, possible_moves[move], element)
        return new_board

    def show_winner(self, final_board: dict, game_winner: str) -> None:

        board = Board()
        print(board.render_board(final_board))
        if board.determine_game_end(final_board) == [i for i in final_board.keys()]:
            print("No winner - play again!")
        else:
            print(f"Congrats {game_winner}!\n")

    def run(self) -> None:

        # get requisite game information
        player_2_type = self.game_setup()

        ## temporary until implementation of computer functionality
        if player_2_type == "computer":
            sys.exit("Computer's aren't supported yet!")
        ## end temporary

        player_1, player_2 = self.get_names(player_2_type)
        player_1_element, player_2_element = self.get_elements(
            player_1, player_2, player_2_type
        )

        # set up initial_board
        board = Board()
        current_board = board.initial_board

        # take turns until game ends
        current_player = player_1
        while not board.determine_game_end(current_board):

            # player turns
            if current_player == player_1:
                current_board = self.make_move(
                    current_board, current_player, player_1_element
                )
                current_player = player_2
            else:
                current_board = self.make_move(
                    current_board, current_player, player_2_element
                )
                current_player = player_1

        game_winner = player_1 if current_player == player_2 else player_2
        self.show_winner(current_board, game_winner)
