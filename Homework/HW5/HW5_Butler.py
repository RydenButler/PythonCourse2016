
class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.size = 1
		self.rev = None
		self.cycle = False

	def length(self):
		return self.size

	def addNode(self, new_value):
		if self.Node(new_value).value is not None:
			self.latest.next = self.Node(new_value)
			self.latest = self.latest.next	
			self.size += 1
			return 'Node added.'
		else:
			return

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

	def closeLink(self):
		self.latest.next = self.head
		self.cycle = True
		return "Linked list has been closed. The cycle is complete!"

	def openLink(self):
		self.latest.next = None
		self.cycle = False
		return "Linked list has been opened. The cycle is broken!"

	def hasCycle(self):
		if self.cycle is True:
			return "This linked list is a cycle."
		else:
			return "This linked list is not a cycle."

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

		def __str__(self):
			return str(self.value)

		def __repr__(self):
			return self.__str__()






chum = LinkedList(1)
chum.addNode(2)
chum.addNode(3)
chum.addNode(3)