import sys
from board import Board
from game import Game


def main():

    # get requisite game information
    game = Game()
    player_2_type = game.game_setup()

    ## temporary until implementation of computer functionality
    if player_2_type == "computer":
        sys.exit("Computer's aren't supported yet!")
    ## end temporary

    player_1, player_2 = game.get_names(player_2_type)
    player_1_element, player_2_element = game.get_elements(
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
            current_board = game.make_move(
                current_board, current_player, player_1_element
            )
            current_player = player_2
        else:
            current_board = game.make_move(
                current_board, current_player, player_2_element
            )
            current_player = player_1

    game_winner = player_1 if current_player == player_2 else player_2
    game.show_winner(current_board, game_winner)


if __name__ == "__main__":
    main()
