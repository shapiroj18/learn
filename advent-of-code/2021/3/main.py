def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content


def parse_gamma_rate(content):
    gamma_rate = ""
    for i in range(len(content[0])):
        bits = [x[i] for x in content]
        gamma_rate += max(bits, key=bits.count)

    return gamma_rate


def parse_epsilon_rate(gamma_rate):
    epsilon_rate = ""
    for i in gamma_rate:
        if i == "0":
            epsilon_rate += "1"
        elif i == "1":
            epsilon_rate += "0"
        else:
            raise AssertionError(f"Invalid bit number: {i}")

    return epsilon_rate


def multiply_decimals(val_1, val_2):

    dec_val1 = int(val_1, 2)
    dec_val2 = int(val_2, 2)

    return dec_val1 * dec_val2


def parse_oxygen_generator_rating(content):
    str_position = 0
    while len(content) > 1:
        bits = [x[str_position] for x in content]
        count_vals = {"zero": bits.count("0"), "one": bits.count("1")}
        digit = "0" if count_vals["zero"] > count_vals["one"] else "1"

        content_removal = [x for x in content if x[str_position] == digit]

        content = list(set(content) - set(content_removal))

        str_position += 1

    return content[0]


def parse_co2_scrubber_rating(content):
    str_position = 0
    while len(content) > 1:
        bits = [x[str_position] for x in content]
        count_vals = {"zero": bits.count("0"), "one": bits.count("1")}
        digit = "0" if count_vals["zero"] <= count_vals["one"] else "1"

        content_removal = [x for x in content if x[str_position] == digit]

        content = list(set(content) - set(content_removal))

        str_position += 1

    return content[0]


def main():
    content = read_file("data.txt")

    gamma_rate = parse_gamma_rate(content)
    epsilon_rate = parse_epsilon_rate(gamma_rate)

    print(f"Question 1: {multiply_decimals(gamma_rate, epsilon_rate)}")

    oxygen_generator_rating = parse_oxygen_generator_rating(content)
    co2_scrubber_rating = parse_co2_scrubber_rating(content)
    print(
        f"Question 2: {multiply_decimals(oxygen_generator_rating, co2_scrubber_rating)}"
    )


if __name__ == "__main__":
    main()
