def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content


def parse_initial_state(content) -> list:
    return [int(x) for x in content[0].split(",")]


def _step(current_state: list) -> list:
    next_state = []
    for i in current_state:
        if i == 0:
            current_fish = 6
            new_fish = 8
            next_state.append(current_fish)
            next_state.append(new_fish)

        else:
            current_fish = i - 1
            next_state.append(current_fish)

    return next_state


def get_final_state(initial_state, number_of_steps: int) -> list:
    this_state = initial_state
    for i in range(number_of_steps):
        next_state = _step(this_state)
        this_state = next_state

    return this_state


def count_number_of_fish(state: list) -> int:
    return len(state)


def main():

    number_of_days = 80

    content = read_file("data.txt")
    initial_state = parse_initial_state(content)
    final_state = get_final_state(initial_state, number_of_days)
    number_of_fish = count_number_of_fish(final_state)
    print(f"The answer to problem 1: {number_of_fish}")


if __name__ == "__main__":
    main()
