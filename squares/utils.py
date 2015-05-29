# helper functions

def calculate_difference(n):
	"""
	This function returns the difference between 
	1.) the square of the sum of the first n natural numbers and
	2.) the sum of the squares of the same n natural numbers 
	"""
	return square_of_sums(n) - sum_of_squares(n)

def square_of_sums(n):
	"""
	This function calculates the square of the sum of
	each natural number that is less than the input n
	"""
	running_sum = 0
	while n > 0:
		running_sum += n
		n -= 1

	return running_sum*running_sum

def sum_of_squares(n):
	"""
	This function calculates the sum of the squares of
	each natural number that is less than the input n
	"""
	running_sum = 0
	while n > 0:
		running_sum += n*n
		n -=1
	return running_sum
	