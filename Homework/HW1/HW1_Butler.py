import datetime
import numpy

class Investment(object):
	def __init__(self, price, ticker):
		self.ticker = str(ticker)
		self.price = float(price)

	def __str__(self):
		return '%s: $%.2f per share' % (self.ticker, self.price)

	def __repr__(self):
		return self.__str__()

class Stock(Investment):
	def __init__(self, price, ticker):
		Investment.__init__(self, int(price), ticker)

class MutualFund(Investment):
	def __init__(self, ticker, price = 1):
		Investment.__init__(self, price, ticker)

class Bond(Investment):
	# This demonstrates how a bond can easily by created as a subclass of Investment by inheriting the generic
	# traits of a price and a name. Without further information on how to handle bonds, they are not further developed
	# here or implemented in the transactions below.
	def __init__(self, price, ticker):
		Investment.__init__(self, price, ticker)


class Portfolio(object):
	def __init__(self, cash = 0):
		self.cash = float(cash)
		self.stock = 'None owned.'
		self.mutual = 'None owned.'
		self.hist = []
		self.original_price = {}

	def __str__(self):
		if type(self.stock) == str:
			stocks = self.stock
		else:
			stocks = []
			for i in self.stock:
				stocks.append('%s - %.2f shares' % (i, self.stock[i]))
			stocks = sorted(stocks)
			stocks = '\n\t'.join(stocks)
		if type(self.mutual) == str:
			mutuals = self.mutual
		else:
			mutuals = []
			for i in self.mutual:
				mutuals.append('%s - %.2f shares' % (i, self.mutual[i]))
			mutuals = sorted(mutuals)
			mutuals = '\n\t'.join(mutuals)
		return 'My portfolio: \nCash: $%.2f \nStocks: \n\t%s \nMutualFunds: \n\t%s' % (self.cash, stocks, mutuals)

	def __repr__(self):
		return self.__str__()

	def addCash(self, benjamins):
		read_out = '$%.2f added to your portfolio.' % benjamins
		self.chronicle(read_out)
		self.cash += float(benjamins)
		return read_out

	def withdrawCash(self, benjamins):
		if benjamins > self.cash:
			print 'Insufficient funds to withdraw $%.2f. \nYour current cash balance is $%.2f.' % (benjamins, self.cash)
		else:
			read_out = '$%.2f withdrawn from your portfolio.' % benjamins
			self.chronicle(read_out)
			self.cash -= float(benjamins)
			return read_out

	def genericBuyer(self, amount, investment, investment_type):
		total = investment.price * amount
		if total > self.cash:
			self.needMore(total - self.cash)
		else:
			self.cash -= total
			if investment_type == 'stock':
				if self.stock == 'None owned.':
					self.stock = {investment.ticker : amount}
				elif investment.ticker in self.stock:
					self.stock[investment.ticker] += amount
				else:
					self.stock[investment.ticker] = amount
			else:
				if self.mutual == 'None owned.':
					self.mutual = {investment.ticker : amount}
				elif investment.ticker in self.mutual:
					self.mutual[investment.ticker] += amount
				else:
					self.mutual[investment.ticker] = amount
			self.original_price[investment.ticker] = investment.price
			read_out = 'Purchased %.2f shares of %s %s at $%.2f/share.' % (amount, investment_type, investment.ticker, investment.price)
			self.chronicle(read_out)
			return read_out

	def buyStock(self, shares, existing_stock):
		if type(existing_stock) != Stock:
			self.wrongType(existing_stock, 'stock')
		if type(shares) != int:
			return "Stocks may only be bought/sold in integer amounts."
		else:
			return self.genericBuyer(shares, existing_stock, 'stock')

	def buyMutualFund(self, shares, existing_mf):
		if type(existing_mf) != MutualFund:
			self.wrongType(existing_mf, 'mutual fund')
		return self.genericBuyer(shares, existing_mf, 'mutual fund')

	def sellStock(self, name, amount):
		if name not in self.stock:
			self.dontOwn('stock')
		elif amount > self.stock[name]:
			self.tooLittle(amount, 'stock', name)
		elif type(amount) != int:
			return "Stocks may only be bought/sold in integer amounts."
		else:
			sale_price = numpy.random.uniform(0.5, 1.5) * self.original_price[name]
			self.cash += sale_price * amount
			if amount < self.stock[name]:
				self.stock[name] -= amount
			else:
				del self.stock[name]
				del self.original_price[name]
			read_out = 'Sold %.2f shares of stock %s at $%.2f/share.' % (amount, name, sale_price)
			self.chronicle(read_out)
			return read_out

	def sellMutualFund(self, name, amount):
		if name not in self.mutual:
			self.dontOwn('mutual fund')
		elif amount > self.mutual[name]:
			self.tooLitte(amount, 'mutual fund', name)
		else:
			sale_price = numpy.random.uniform(0.9,1.2)
			self.cash += sale_price * amount
			if amount < self.mutual[name]:
				self.mutual[name] -= amount
			else:
				del self.mutual[name]
			read_out = 'Sold %.2f shares of mutual fund %s at $%.2f/share.' % (amount, name, sale_price)
			self.chronicle(read_out)
			return read_out

	# Two functions to record and recall history

	def chronicle(self, info):
		timestamp = datetime.datetime.now().strftime("%I:%M%p on %m/%d/%Y")
		self.hist.insert(0, '%s - %s' % (timestamp, info))

	def history(self):
		ordered_history = '\n\t'.join(self.hist)
		return 'Your transaction history (most recent transactions listed first): \n\n\t%s' % ordered_history

	# The following functions inform the user of errors.

	def needMore(self, diff):
		return 'Unable to complete transaction: The total price of the purchase exceeds the cash in your portfolio. You will need to add $%.2f more before making this purchase.' % diff

	def wrongType(self, investment, investment_type):
		return 'Error: %s is not an existing %s!' %(investment.ticker, investment_type)

	def dontOwn(self, investment_type):
		return 'Error: You have not invested in any %ss matching that name.' % investment_type

	def tooLittle(self, amount, investment_type, ticker):
		if investment_type == 'stock':
			return 'Error: You do not own %.2f shares of %s %s. The maximum you may sell is %.2f' % (amount, investment_type, ticker, self.stock[ticker])
		else:
			return 'Error: You do not own %.2f shares of %s %s. The maximum you may sell is %.2f' % (amount, investment_type, ticker, self.mutual[ticker])





		




