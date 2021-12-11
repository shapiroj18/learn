import math


def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content


def parse_lines(content) -> list:
    all_coords = []
    for line in content:
        line_list = line.split()
        x1, y1 = line_list[0].split(",")
        x2, y2 = line_list[2].split(",")
        all_coords.append([int(x1), int(y1), int(x2), int(y2)])

    return all_coords


def gen_all_multiple_coords(coords: list) -> list:
    """
    Generate list of all coordinates, then they can be counted
    """

    coords_list = []
    for i in coords:
        x1, y1, x2, y2 = i
        if x1 == x2:
            if y1 > y2:
                for j in range(y2, y1 + 1):
                    coords_list.append([x1, j])

            elif y1 < y2:
                for j in range(y1, y2 + 1):
                    coords_list.append([x1, j])

        elif y1 == y2:
            if x1 > x2:
                for j in range(x2, x1 + 1):
                    coords_list.append([j, y1])

            elif x1 < x2:
                for j in range(x1, x2 + 1):
                    coords_list.append([j, y1])

        else:
            x_diff = max([x1, x2]) - min([x1, x2])
            y_diff = max([y1, y2]) - min([y1, y2])

            if x_diff != 0 and y_diff != 0:
                if math.degrees(math.atan(x_diff / y_diff)) == 45.0:
                    x_dir = "positive" if x1 < x2 else "negative"
                    y_dir = "positive" if y1 < y2 else "negative"

                    if x_dir == "positive" and y_dir == "positive":

                        for i in range(x1, x2 + 1):

                            coords_list.append([x1, y1])
                            x1 += 1
                            y1 += 1

                    elif x_dir == "positive" and y_dir == "negative":

                        for i in range(x1, x2 + 1):
                            coords_list.append([x1, y1])
                            x1 += 1
                            y1 -= 1

                    elif x_dir == "negative" and y_dir == "positive":

                        for i in range(x2, x1 + 1):
                            coords_list.append([x1, y1])
                            x1 -= 1
                            y1 += 1

                    elif x_dir == "negative" and y_dir == "negative":

                        for i in range(x2, x1 + 1):
                            coords_list.append([x1, y1])
                            x1 -= 1
                            y1 -= 1

    multiple_coords = []
    for i in coords_list:
        if coords_list.count(i) >= 2:
            multiple_coords.append(i)

    non_duplicate_multiple_coords = []
    for i in multiple_coords:
        if i not in non_duplicate_multiple_coords:
            non_duplicate_multiple_coords.append(i)

    return non_duplicate_multiple_coords


def main():
    content = read_file("data.txt")
    all_coords = parse_lines(content)

    final_coords = gen_all_multiple_coords(all_coords)

    print(f"Question 1: {len(final_coords)}")


if __name__ == "__main__":
    main()
