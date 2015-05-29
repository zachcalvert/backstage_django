from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from models import Calculation
from utils import calculate_difference, square_of_sums, sum_of_squares

class CalculationTest(TestCase):
	"""
	Ensure that our calculation utility functions work as expected
	"""

	def test_square_of_sums(self):
		"""
		The sum of the squares of the first 10 natural numbers is 3025 (given)
		"""
		self.assertEqual(square_of_sums(10), 3025)

	def test_sum_of_squares(self):
		"""
		The sum of the squares of the first 10 natural numbers is 385 (given)
		"""
		self.assertEqual(sum_of_squares(10), 385)

	def test_calculate_difference(self):
		"""
		The calculated difference between the above functions with input 10 is 2640 (given)
		"""
		self.assertEqual(calculate_difference(10), 2640)



# class ServiceTest(TestCase):
# 	"""
# 	Do some shit
# 	"""
# 	def setUp(self):
# 		"""
#         Create some test numbers with history
#         """
#         Calculation.objects.create(number=1, value=1, occurrences=3)
#         Calculation.objects.create(number=10, value=2640, occurrences=5)

# 	def test_service_endpoint(self):
# 		c = Client()
# 		response = c.get('/difference?=10')
# 		self.assertEqual(response.status_code, 200)
