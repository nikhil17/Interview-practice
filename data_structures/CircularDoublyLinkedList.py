from node import Node2
from SinglyLinkedList import MyList
import unittest

class CircularDoublyLinkedList(MyList):
	def __init__(self):
		super(CircularDoublyLinkedList, self).__init__()

	def iterate_nodes(self):
		curr, x = self.head, 0
		while (x < self.size):
			yield curr
			curr, x = curr.next, x + 1

	def add(self, value):
		node = Node2(value)
		if (self.head == None):
			self.head = self.tail = node
		else:
			oldTail = self.tail
			oldTail.next, node.prev = node, oldTail
			self.head.prev, node.next = node, self.head
			self.tail = node

		self.size += 1

	def remove (self, value):
		found = False
		if self.head.value is value:
			found = True
			if self.size is 1:
				self.head = self.tail = None
			n = self.head.next
			self.tail.next, n.prev = n, self.tail
			self.head = n

		elif self.tail.value is value:
			found = True
			nTail = self.tail.prev
			nTail.next, self.head.prev = self.head, nTail
		else:
			current = self.head.next
			while (current is not self.tail and not found):
				if current.value is value:
					found = True
					p, n = current.prev, current.next
					p.next, n.prev = n, p
					
				current = current.next

		if found:
			self.size -= 1
		else:
			print str(value) + ' is not in the list'

class CircularTests(unittest.TestCase):
	def checkAddRemove(self):
		l = CircularDoublyLinkedList()
		l.add(3)
		l.add(4)
		l.add(5)
		l.add(4)
		self.assertEqual(l.listify(), [3,4,5,4])


if __name__ == '__main__':
    unittest.main()
