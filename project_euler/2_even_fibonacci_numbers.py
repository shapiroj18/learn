# https://projecteuler.net/problem=2

x = 0
y = True
list = [1]
max_value = 4e6


while y:

	ele = list[x] + list[x - 1]
	list.append(ele)

	x += 1

	test_ele = list[x] + list[x - 1]
	if test_ele > max_value:
		y = False


sum = 0
for i in list:
	if i % 2 == 0:
		sum += i

print(sum)
