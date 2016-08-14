import unittest
from HW1_Butler import *

portfolio = Portfolio()
s = Stock(20, "HFH")
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

class HW1Test(unittest.TestCase):

	def test_addCash(self):
		self.assertEqual("$300.50 added to your portfolio.", portfolio.addCash(300.50))
		self.assertEqual(300.50, portfolio.cash)

	def test_buyStock(self):
		self.assertEqual('Purchased 5.00 shares of stock HFH at $20.00/share.', portfolio.buyStock(5, s))
		self.assertEqual({"HFH": 5}, portfolio.stock)

	def test_buyMF(self):
		self.assertEqual('Purchased 10.30 shares of mutual fund BRT at $1.00/share.', portfolio.buyMutualFund(10.3, mf1))
		self.assertEqual({"BRT": 10.30}, portfolio.mutual)

	def test_buyMF2(self):
		self.assertEqual('Purchased 2.00 shares of mutual fund GHT at $1.00/share.', portfolio.buyMutualFund(2, mf2))
		self.assertEqual({"BRT": 10.30, "GHT": 2.00}, portfolio.mutual)

	def test_sellMF(self):
		portfolio.sellMutualFund("BRT", 3)
		self.assertEqual(7.30, portfolio.mutual["BRT"])
	# The above test fails, but it is merely a result of the way python stores floats. The numbers are equivalent.

	def test_sellStock(self):
		portfolio.sellStock("HFH", 1)
		self.assertEqual(4, portfolio.stock["HFH"])

	def test_withdraw(self):
		cash_now = portfolio.cash
		portfolio.withdrawCash(50)
		self.assertEqual(cash_now - 50, portfolio.cash)

if __name__ == '__main__':
	unittest.main()