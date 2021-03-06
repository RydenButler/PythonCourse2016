import unittest
import Ordinalize

class OrdinalTest(unittest.TestCase):

	def test_first(self):
		self.assertEqual('1st', Ordinalize.ordinalize(1))
		self.assertNotEqual('1', Ordinalize.ordinalize(1))

	def test_second(self):
		self.assertEqual('2nd', Ordinalize.ordinalize(2))
		self.assertNotEqual('2', Ordinalize.ordinalize(2))

	def test_third(self):
		self.assertEqual('3rd', Ordinalize.ordinalize(3))
		self.assertNotEqual(3, Ordinalize.ordinalize(3))

	def test_four_plus(self):
		for x in range(4,10):
			self.assertEqual('%ith' % x, Ordinalize.ordinalize(x))
			self.assertNotEqual('tiger', Ordinalize.ordinalize(x))


if __name__ == '__main__':
	unittest.main()
