from node import Node

class SinglyLinkedList(object):

	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def add(self,value):
		if not self.head:
			self.head = Node(value)
			self.tail = self.head
		else:
			n = Node(value)
			self.tail.next = n
			self.tail = n

		self.size += 1

	def addToHead(self, value):
		n = Node(value)
		if self.head:
			n.next = self.head
		self.head, self.size = n, self.size + 1

	def list(self):
		return self
	
	# returns an iterator of the nodes in the list
	def iterateNodes(self):
		n, i = self.head, 0
		while (i < self.size):
			yield n
			n, i = n.next, i + 1


	def getNodeAtIndex(self, index):
		if (index > self.size):
			print 'Invalid Index'
			return None
		i, n = 0, self.head
		# while (i< self.size):



	def printList(self):
		print 'using generator'
		for n in self.iterateNodes():
			print n.value
	
	# searches for 
	def deleteNodeValue(self, value):
		current = self.head
		prev = None
		found = False
		if self.head.value == value:
			found = True
			self.head = current.next
			self.size -= 1
		else:
			while current and not found:
				if (current.value == value):
					prev.next = current.next
					found = True
					self.size -= 1
					continue

				
				prev = current
				current = current.next

		if not found:
			print 'Node with given value is not in list'


x = SinglyLinkedList()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(5)
x.printList()
x.addToHead(0)
x.printList()
x.deleteNodeValue(0)
x.deleteNodeValue(5)

x.printList()
