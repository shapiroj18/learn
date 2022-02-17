from board import Board

class Computer:
    def __init__(self):
        ...
        
    def determine_move_random(self, board: dict) -> str:
        
        board_module = Board()
        
        possible_computer_moves = []
        for board_position, filled_in_value in board.items():
            if filled_in_value is not None:
                possible_computer_moves.append(board_position)
                
        # if length of possible_computer_moves is 0
        
        if len(possible_computer_moves) == 0 and not board.determine_game_end(board_module):
            raise Exception("Determined total computer moves available are none, but game is not over")
        
        
        
        # get a random value from the possible computer moves
        # return computer moves