import unittest
import random
from HW4_Ryden import *

first_ten = [1,2,3,4,5,6,7,8,9,10,10]
jumbled_ten = [10,2,6,5,8,9,1,3,4,7,10]

random_ten = []
for i in range(10):
	random_ten.append(int(random.uniform(1,100)))
sorted(random_ten)


class HW4Test(unittest.TestCase):

	def test_Insertion(self):
		self.assertEqual(first_ten, Insertion_Sort(jumbled_ten))
		self.assertEqual(sorted(random_ten), Insertion_Sort(random_ten))

	def test_Merge(self):
		self.assertEqual(first_ten, Merge_Sort(jumbled_ten))
		self.assertEqual(sorted(random_ten), Merge_Sort(random_ten))


if __name__ == '__main__':
	unittest.main()