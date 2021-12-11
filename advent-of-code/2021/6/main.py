import collections


def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content


def parse_initial_state(content) -> collections.Counter:
    return collections.Counter([int(x) for x in content[0].split(",")])


def get_final_state(initial_state: collections.Counter, number_of_steps: int) -> list:
    counter = initial_state
    for _ in range(number_of_steps):
        counter2 = collections.Counter({6: counter[0], 8: counter[0]})
        for i, j in counter.items():
            if i > 0:
                counter2[i - 1] += j
        counter = counter2

    return counter


def count_number_of_fish(state: collections.Counter) -> int:
    return sum(state.values())


def main():

    number_of_days = 256

    content = read_file("data.txt")
    initial_state = parse_initial_state(content)
    final_state = get_final_state(initial_state, number_of_days)
    number_of_fish = count_number_of_fish(final_state)
    print(f"The answer to problem 1: {number_of_fish}")


if __name__ == "__main__":
    main()
