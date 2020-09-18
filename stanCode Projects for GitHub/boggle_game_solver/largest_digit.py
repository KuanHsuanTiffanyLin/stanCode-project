"""
stanCode SC101 Assignment 5 Problem 3
File: largest_digit.py
Name: Tiffany Lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	The largest digit in integer inserted in the function, "find_largest_digit", will be found
	by recursion and printed on Console.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, a number input by the user
	:return: the largest digit in n
	"""
	if 0 <= n < 10:
		return n
	else:
		if n < 0:
			return find_largest_digit(-n)
		else:
			if (n % 10) <= ((n % 100 - n % 10)/10):
				return find_largest_digit((n-n % 10)//10)
			else:
				return find_largest_digit((n//10) - ((n//10) % 10) + (n % 10))


if __name__ == '__main__':
	main()
