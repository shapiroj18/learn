def read_file(file_path: str) -> list:
    
    f = open(file_path)
    content = f.read().splitlines()
    
    return content

def parse_content(content: list) -> list:
    
    vectors = []
    for i in content:
        instruction = [x for x in i.split()]
        vectors.append(instruction)
    
    return vectors

def calculate_final_position_1(vectors: list) -> tuple:
    
    x_position = 0
    y_position = 0
    
    for i in vectors:
        command = i[0]
        delta = int(i[1])
        
        if command == 'forward':
            x_position += delta
        elif command == 'down':
            y_position += delta
        elif command == 'up':
            y_position -= delta
        else:
            raise ValueError(f'Unknown command: {command}')
        
    return x_position, y_position

def calculate_final_position_2(vectors: list) -> tuple:
    
    x_position = 0
    y_position = 0
    aim = 0
    
    for i in vectors:
        command = i[0]
        delta = int(i[1])
        
        if command == 'forward':
            x_position += delta
            y_position += aim * delta
            print(f'forward: {x_position, y_position, aim}')
        elif command == 'down':
            aim += delta
            print(f'down: {x_position, y_position, aim}')
        elif command == 'up':
            aim -= delta
            print(f'up: {x_position, y_position, aim}')
        else:
            raise ValueError(f'Unknown command: {command}')
        
    return x_position, y_position

def multiply_positions(x_position, y_position):
    
    return x_position * y_position

def main():
    raw_data = read_file('data.txt')
    parsed = parse_content(raw_data)
    
    x_position_1, y_position_1 = calculate_final_position_1(parsed)
    print(f'Question 1: {multiply_positions(x_position_1, y_position_1)}')
    
    x_position_2, y_position_2 = calculate_final_position_2(parsed)
    print(f'Question 2: {multiply_positions(x_position_2, y_position_2)}')

if __name__ == "__main__":
    main()