# https://projecteuler.net/problem=7

def _is_prime(num: int) -> bool:
	if num == 1:
		return False
	else:
		for i in range(2, num - 1):
			if num % i == 0:
				return False
		
		else:
			return True
			
def get_primes(num: int):
 
	primes_list = []
	i = 1
	while len(primes_list) < num:
		if _is_prime(i):
			primes_list.append(i)
			print(primes_list[-5:])
		i += 1

	return primes_list
  
  
def main():
	prime_list = get_primes(10001)
	print(f'The final prime is: {prime_list[-1]}')

if __name__ == '__main__':
    main()
