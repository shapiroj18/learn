# https://projecteuler.net/problem=6
numbers = range(1, 101)
sum_numbers = sum(numbers)

squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)


print(sum_numbers ** 2 - sum(squares))
