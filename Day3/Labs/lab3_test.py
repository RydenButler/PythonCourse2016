import unittest
import lab3_Ryden

class LabTest(unittest.TestCase):
	
	def test_shout(self):
		self.assertEqual("STOP YELLING!!!", lab3_Ryden.shout('stop yelling'))
		with self.assertRaises(TypeError):
			lab3_Ryden.shout(4)

	def test_reverse(self):
		self.assertEqual("!esrever", lab3_Ryden.reverse('reverse!'))
		self.assertEqual('gib < elttil', lab3_Ryden.reverse('big > little'))
		self.assertEqual('gib & elttil', lab3_Ryden.reverse('big & little'))	
		with self.assertRaises(TypeError):
			lab3_Ryden.reverse(4)


	def test_reversewords(self):
		self.assertEqual('reverse!', lab3_Ryden.reversewords('reverse!'))
		self.assertEqual('little > big', lab3_Ryden.reversewords('big > little'))
		self.assertEqual('little & big', lab3_Ryden.reversewords('big & little'))
		with self.assertRaises(TypeError):
			lab3_Ryden.reversewords(4)

	def test_reversewordletters(self):
		self.assertEqual('!esrever', lab3_Ryden.reversewordletters('reverse!'))
		self.assertEqual('elttil < gib', lab3_Ryden.reversewordletters('big > little'))
		self.assertEqual('elttil & gib', lab3_Ryden.reversewordletters('big & little'))
		with self.assertRaises(TypeError):
			lab3_Ryden.reversewordletters(4)

	def test_piglatin(self):
		self.assertEqual("ig-pay atin-lay ing-stray", lab3_Ryden.piglatin('pig latin string'))
		self.assertNotEqual("ig-pay atin-lay tring-say", lab3_Ryden.piglatin('pig latin string'))
		with self.assertRaises(TypeError):
			lab3_Ryden.piglatin(4)

if __name__ == '__main__':
	unittest.main()