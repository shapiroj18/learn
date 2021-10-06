# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np

two_digit_list = []
for i in range(100, 1000):
	two_digit_list.append(i)

a = two_digit_list.copy()
b = two_digit_list.copy()

products = []
for i in a:
	for j in b:
		products.append(i * j)


product_boolean = []
for i in products:
	if len(str(i)) % 2 == 0:
		if str(i)[:int(len(str(i))/2)] == str(i)[-int(len(str(i))/2):][::-1]:
			product_boolean.append(True)
		else:
			product_boolean.append(False)
	else:
		if str(i)[:int(len(str(i))/2) + 1] == str(i)[- int(len(str(i))/2) - 1:][::-1]:
			product_boolean.append(True)
		else:
			product_boolean.append(False)



products_array = np.array(products)
filter = np.array(product_boolean)

print(max(products_array[filter]))