# https://projecteuler.net/problem=3
import math


number = 600851475143

list = []
print('-----individual_factors-----')
for i in range(1, int(math.sqrt(number))):
	if number % i == 0:
		print(i)
		list.append(i)
		
print('-----factors_list-----')
print(list)
print('-----individual_primes-----')

primes_list = []
for j in list:
	sub_list = []
	for k in range(1, j+1):
		if j % k == 0:
			sub_list.append(k)
		
	if sub_list == [1, j]:
		print(j)
		primes_list.append(j)


print('-----max_prime-----')
print(max(primes_list))
