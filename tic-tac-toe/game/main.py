from board import Board

def main():
    
    # while True until game ends
    
    board = Board()
    current_board = board.fill_board_value(board.initial_board, 'row_1_col_1', "X")
    current_board = board.fill_board_value(current_board, 'row_1_col_2', "O")
    current_board = board.fill_board_value(current_board, 'row_2_col_1', "X")
    current_board = board.fill_board_value(current_board, 'row_2_col_2', "O")
    current_board = board.fill_board_value(current_board, 'row_3_col_1', "X")

    print(board.render_board(current_board))

if __name__ == "__main__":
    main()