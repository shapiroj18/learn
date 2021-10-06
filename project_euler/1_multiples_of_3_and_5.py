# https://projecteuler.net/problem=1

list = []

for number in range(0, 1000):

	if number % 3 == 0 or number % 5 == 0:
		list.append(number)

total = 0

for element in list:
	total += element

print(total)
