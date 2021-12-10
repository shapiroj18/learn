import numpy as np


def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content


def parse_caller_input(content) -> list:

    return content[0].split(",")


def parse_bingo_arrays(content) -> list:
    array_items = []
    for line in content[1:]:
        line_list = line.split()
        if len(line_list):
            array_item = np.array(line_list)
            array_items.append([array_item])

    np_array_tot = np.concatenate(tuple([i for i in array_items]), axis=0)

    bingo_boards = np.split(np_array_tot, len(np_array_tot) / 5)

    return bingo_boards


def test_winner(caller_input, bingo_board):
    for i in bingo_board:
        if set(i).issubset(caller_input):
            return True

    for i in bingo_board.transpose():
        if set(i).issubset(caller_input):
            return True


def find_winner(caller_input, bingo_boards):

    counter = 0
    while counter <= len(caller_input):
        current_nums = caller_input[:counter]
        for i in bingo_boards:
            if test_winner(current_nums, i):
                return current_nums, i
        counter += 1


def find_loser_board(caller_input, bingo_boards):

    counter = 0
    all_boards = bingo_boards.copy()
    while counter <= len(caller_input):
        current_nums = caller_input[:counter]
        for i, x in enumerate(all_boards):
            if test_winner(current_nums, x):
                all_boards.pop(i)

        if len(all_boards) == 1:
            return all_boards[0]
        counter += 1


def find_loser_counter(caller_input, bingo_board):

    for i in range(len(caller_input)):
        if test_winner(caller_input[:i], bingo_board):
            return caller_input[:i]


def get_score(caller_input, bingo_board):

    board_nums = []
    for i in bingo_board:
        for x in i:
            board_nums.append(x)

    board_nums_int = [int(i) for i in board_nums]
    caller_input_int = [int(i) for i in caller_input]
    unmarked_sum = sum(set(board_nums_int) - set(caller_input_int))
    last_caller_input = caller_input_int[-1]

    return unmarked_sum * last_caller_input


def main():
    content = read_file("data.txt")

    parsed_caller_input = parse_caller_input(content)
    parsed_bingo_arrays = parse_bingo_arrays(content)

    final_caller_input, bingo_winner = find_winner(
        parsed_caller_input, parsed_bingo_arrays
    )

    print(f"Question 1: {get_score(final_caller_input, bingo_winner)}")

    bingo_loser = find_loser_board(parsed_caller_input, parsed_bingo_arrays)

    final_caller_input = find_loser_counter(parsed_caller_input, bingo_loser)

    print(f"Question 2: {get_score(final_caller_input, bingo_loser)}")


if __name__ == "__main__":
    main()
