def read_file(file_path: str) -> list:
    f = open(file_path)
    content = f.read().splitlines()

    data = []
    for line in content:
        data.append(int(line))

    return data


def answer_increase_decrease_1(data_floor_depth: list):

    answers = []
    for i, x in enumerate(data_floor_depth):
        if i == 0:
            answers.append("(N/A - no previous measurement)")
        elif data_floor_depth[i] > data_floor_depth[i - 1]:
            answers.append("(increased)")
        else:
            answers.append("(decresed)")

    return answers


def answer_increase_decrease_2(data_floor_depth: list):

    answers = []
    for i, x in enumerate(data_floor_depth):
        if i == 0:
            answers.append("(N/A - no previous measurement)")
        elif i < len(data_floor_depth) - 2:
            sum_last = sum(
                [data_floor_depth[i - 1], data_floor_depth[i], data_floor_depth[i + 1]]
            )
            sum_current = sum(
                [data_floor_depth[i], data_floor_depth[i + 1], data_floor_depth[i + 2]]
            )

            if sum_current > sum_last:
                answers.append("(increased)")
            elif sum_current == sum_last:
                answers.append("(no change)")
            else:
                answers.append("(decreased)")

    return answers


def count_increases(answers: list) -> int:

    total = answers.count("(increased)")

    return total


def main_1():

    raw_data = read_file("data.txt")
    answers = answer_increase_decrease_1(raw_data)
    total_count = count_increases(answers)

    return total_count


def main_2():

    raw_data = read_file("data.txt")
    answers = answer_increase_decrease_2(raw_data)
    total_count = count_increases(answers)

    return total_count


if __name__ == "__main__":
    print(f"The answer to question 1: {main_1()}")
    print(f"The answer to question 2: {main_2()}")
