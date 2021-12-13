import statistics

def read_file(file_path: str) -> list:

    f = open(file_path)
    content = f.read().splitlines()

    return content

def parse_content(content: list) -> list:
    parsed_strings = content[0].split(',')
    parsed_ints = [int(i) for i in parsed_strings]
    return parsed_ints

def get_median(content) -> int:
    return int(statistics.median(content))

def _get_fuel(position: int, median: int) -> int:
    return abs(position - median)

def get_total_fuel(content: list, median: int) -> int:
    sum = 0
    for i in content:
        amount = _get_fuel(i, median)
        sum += amount
        
    return sum

def main():
    content = read_file('data.txt')
    parsed_content = parse_content(content)
    median = get_median(parsed_content)
    total_fuel = get_total_fuel(parsed_content, median)
    print(f'Question 1 answer: {total_fuel}')

if __name__ == '__main__':
    main()