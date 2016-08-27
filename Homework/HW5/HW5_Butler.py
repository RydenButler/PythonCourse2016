
class LinkedList():

	def __init__(self, value):
		self.head = self.Node(value)
		self.latest = self.head
		self.rev = None

	def length(self):
		tally = 1
		node = self.head
		while node.next is not None:
			tally +=1
			node = node.next
		return tally

	def addNode(self, new_value):
		self.latest.next = self.Node(new_value)
		self.latest = self.latest.next	
		return 'Node added.'

	def addNodeAfter(self, new_value, after_node):
		tally = 1
		node = self.head
		while tally != after_node:
			tally += 1
			node = node.next
		move_after = node.next
		node.next = self.Node(new_value)
		node.next.next = move_after
		return 'Added new node after node %d.' % after_node

	def addNodeBefore(self, new_value, before_node):
		if before_node == 1:
			move_after = self.head
			self.head = self.Node(new_value)
			self.head.next = move_after
		else:
			self.addNodeAfter(new_value, before_node - 1)
		return 'Added new node before node %d.' % before_node

	def removeNode(self, node_to_remove):
		if node_to_remove == 1:
			self.head = self.head.next
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
		return 'Removed node %d.' % node_to_remove 

	def removeNodesByValue(self, value):
		tally = 1
		node = self.head
		try:
			while node.value != value:
				tally += 1
				node = node.next
			self.removeNode(tally)
			self.removeNodesByValue(value)
		except AttributeError:
			return 'Removed all nodes with value %d.' % value

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
		self.reverse()


	def __str__(self):
		node = self.head
		for i in range(1,self.length()+1):
			print '''
Node %d: %d
   ||
   \/''' % (i, node.value)
			node = node.next
		return ''

	def __repr__(self):
		return self.__str__()
	
	#def hasCycle(self:)

	class Node:
		def __init__(self, _value=None, _next=None):
			self.value = _value
			self.next = _next
		def __str__(self):
			return str(self.value)

		def __repr__(self):
			return self.__str__()






chum = LinkedList(1)
chum.addNode(2)
chum.addNode(3)