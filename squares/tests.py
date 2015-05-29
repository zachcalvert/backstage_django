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



class ServiceTest(TestCase):
	"""
	Verify the constructed endpoint is available and returns data in the
	expected format
	"""
	def setUp(self):
		"""
		The test db seems to be reading the same data as the "live" db, 
		hence the get_or_creates
        """
        Calculation.objects.get_or_create(number=1, value=0) # correct value
        Calculation.objects.get_or_create(number=10, value=2640)
        Calculation.objects.get_or_create(number=100, value=25164150)

	def test_service_endpoint(self):
		response = self.client.get("%s?number=1" % reverse('get_difference'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(1, Calculation.objects.get(number=1).occurrences)

		# self.assertContains(response.content, "number")
		# self.assertContains(response.content, "value"
		# self.assertContains(response.content, "occurrences"
		# self.assertContains(response.content, "last_requested"

		response = self.client.get("%s?number=1" % reverse('get_difference'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(2, Calculation.objects.get(number=1).occurrences)

	# def test_occurrences_incrementor(self):
	# 	"""
	# 	The number of occurrences for a given Calculation instance should 
	# 	increase by 1 after a successful request to that resource
	# 	"""
	# 	count = Calculation.objects.get(number=1, value=1).occurrences

	# 	response = self.client.get("%s?number=1" % reverse('get_difference'))
	# 	self.assertEqual(response.status_code, 200)

	# 	self.assertEqual(count+1, Calculation.objects.get(number=1).occurrences)





