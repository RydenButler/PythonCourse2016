
class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.size = 1
		self.rev = None
		self.cycle = False

	# O(1): Length only requires a return statement, the time complexity is constant. This is maximally efficient.
	def length(self):
		return self.size

	# O(1): addNode also has constant complexity because adding a single node requires the same amount of time, regardless
	# of the number of other existing nodes. This is maximally efficient.
	def addNode(self, new_value):
		if self.Node(new_value).value is not None:
			self.latest.next = self.Node(new_value)
			self.latest = self.latest.next	
			self.size += 1
			return 'Node added.'
		else:
			return

	# O(n): Though adding the node is constant, iterating over existing nodes takes at best 0, and at worst n, iterations.
	# Since the average number of iterations is n/2, we can simplify the notation to O(n). The only way to improve efficieny
	# would be to remove the iterative process. I'm not sure if this is possible, given the task?
	def addNodeAfter(self, new_value, after_node):
		if type(after_node) is not int:
			print "Node number must be an integer value. I'll try and convert it for you by rounding down!"
			try:
				after_node = int(after_node)
			except:
				return "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
		if self.Node(new_value).value is not None:
			tally = 1
			node = self.head
			while tally != after_node:
				tally += 1
				node = node.next
			move_after = node.next
			node.next = self.Node(new_value)
			node.next.next = move_after
			self.size += 1
			return 'Added new node after node %d.' % after_node
		else:
			return

	# O(n): Like the previous function (which is called herein), the average function call must undergo n/2 (simplified to O(n)
	# iterations. At best the function is O(1).
	def addNodeBefore(self, new_value, before_node):
		if type(before_node) is not int:
			print "Node number must be an integer value. I'll try and convert it for you by rounding down!"
			try:
				before_node = int(before_node)
			except:
				return "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
		if self.Node(new_value).value is not None:
			if before_node == 1:
				move_after = self.head
				self.head = self.Node(new_value)
				self.head.next = move_after
				self.size += 1
			else:
				self.addNodeAfter(new_value, before_node - 1)
				self.size += 1
			return 'Added new node before node %d.' % before_node
		else:
			return

	# O(n): As with the adding functions, the best case (removing the first node) is a constant operation. However the average
	# function call requires 2 iterations, that, at worst, makes the complexity 2n (simplified to O(n)). Therefore the average 
	# call is O(n). As with the adding functions, the only way to improve the efficieny would require removing the iterative 
	# component of the function, which I'm not sure is even possible. 
	def removeNode(self, node_to_remove):
		if type(node_to_remove) is not int:
			print "Node number must be an integer value. I'll try and convert it for you by rounding down!"
			try:
				node_to_remove = int(node_to_remove)
			except:
				return "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
		if node_to_remove == 1:
			self.head = self.head.next
			self.size -= 1
		else:
			tally = 1
			node = self.head
			while tally != node_to_remove:
				tally += 1
				node = node.next
			move_after = node.next
			tally = 1
			node = self.head
			while tally != node_to_remove-1:
				tally += 1
				node = node.next
			node.next = move_after
			self.size -= 1
		return 'Removed node %d.' % node_to_remove 

	# O(n^2): Removing nodes by values requires iterating over n nodes n times, depending on how many nodes of a given value
	# exist within the linked list. This is caused by the recursive iteration over all nodes. I suppose the efficient could
	# be improved to O(n) if there were some way of iterating over the list once and performing necessary node removals in place 
	#before moving to the next node.
	def removeNodesByValue(self, value):
		if type(value) is not int:
			print "Node data must be an integer value. I'll try and convert it for you by rounding down!"
		try:
			value = int(value)
		except:
			return "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
		tally = 1
		node = self.head
		while node.value != value and node.next != None:
			tally += 1
			node = node.next
		if tally == self.length() and node.value != value:
			return "Removed all nodes with value %d" % value
		else:
			self.removeNode(tally)
			return self.removeNodesByValue(value)

	# O(n!): Reversing the list requires iterating over the original list until the final node is reached, creating a new
	# link in the reversed list over each iteration. Therefore n! iterations are computed in the creation of the reversed
	# list. Since O(n!) is very high complexity, the efficiency could likely be improved. Perhaps a function that iterates
	# over the list of nodes one time and reverses node.value and node.next for each node would be superior.

	def reverse(self):
		node = self.head
		new = self.rev
		if node is None:
			self.head = self.rev
			self.rev = None
			return 'Nodes reversed.'
		forward_tally = 1
		while node.next is not None:
			forward_tally += 1
			node = node.next
		if new is None:
			self.rev = self.Node(node.value)
		else:
			reverse_tally = 1
			while new.next is not None:
				reverse_tally += 1
				new = new.next
			new.next = self.Node(node.value)
		self.removeNode(forward_tally)
		return self.reverse()

	# O(1): Assigning the .next value of the last node is a constant operation. Maximally efficient
	def closeLink(self):
		self.latest.next = self.head
		self.cycle = True
		return "Linked list has been closed. The cycle is complete!"

	# O(1): Similar to the previous function.
	def openLink(self):
		self.latest.next = None
		self.cycle = False
		return "Linked list has been opened. The cycle is broken!"

	# O(1): As the two previous functions, a constant operation that checks the boolean self.cycle
	def hasCycle(self):
		if self.cycle is True:
			return "This linked list is a cycle."
		else:
			return "This linked list is not a cycle."

	# O(n): Iterates over the node list one time to print all nodes and values.
	def __str__(self):
		node = self.head
		for i in range(1,self.length()+1):
			print '''
Node %d: %d
   ||
   \/''' % (i, node.value)
			node = node.next
		if self.cycle is True:
			print '''
Node 1: %d
   ||
   \/''' % self.head.value
		return ''

	# O(n): Calls self.__str__(), which is O(n) complex.
	def __repr__(self):
		return self.__str__()



	class Node:
		def __init__(self, _value=None, _next=None):
			if type(_value) is not int:
				print "Node data must be an integer value. I'll try and convert it for you by rounding down!"
			try:
				self.value = int(_value)
			except:
				self.value = None
				print "I can only convert floats and numeric strings to integers. Please try again with a valid input type."
			self.next = _next

		# O(1): Returns a single value for each node. Constant; maximally efficient.
		def __str__(self):
			return str(self.value)

		# O(1): Calls the previous function.
		def __repr__(self):
			return self.__str__()