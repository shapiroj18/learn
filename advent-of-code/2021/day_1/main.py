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
            answers.append('(N/A - no previous measurement)')
        elif data_floor_depth[i] > data_floor_depth[i-1]:
            answers.append('(increased)')
        else:
            answers.append('(decresed)')
    
    return answers


def count_increases_1(answers: list) -> int:
    
    total = answers.count('(increased)')
    
    return total

def main_1():
    
    raw_data = read_file('data.txt')
    answers = answer_increase_decrease_1(raw_data)
    total_count = count_increases_1(answers)
    
    return total_count
    

if __name__ == '__main__':
    exit(print(main_1()))