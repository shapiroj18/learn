# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# this solution is very brute force - is there a better way?
   
i = 2

def check_remainder(input, num):
    return input % num == 0
    

while True:
	if all([check_remainder(i, x) for x in range(1, 21)]):
		print(i)
		break
	else:
		# can't be odd
		i += 2
		print(f'not it: {i}')
