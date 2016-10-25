from node import Node
import unittest

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
		curr = self.head
		while (curr):
			yield curr
			curr = curr.next


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

	def listify(self):
		x = list()
		for n in self.iterateNodes():
			x.append(n.value)
		return x

	def contains(self, value):
		for n in self.iterateNodes():
			if n.value is value:
				return True
		return False
	
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
		if found and current == self.tail:
			self.tail = prev

		if not found:
			print 'Node with given value is not in list'


class UnitTestSinglyLinkedList(unittest.TestCase):
	def testAdd(self):
		s = SinglyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)
		# print s.listify()
		self.assertEqual(s.listify(), [1,2,3])
		s.addToHead(99)
		self.assertEqual(s.listify(), [99,1,2,3])
		
		s.deleteNodeValue(3)
		print s.listify()
		s.add(10)
		print 'added 10'
		print s.listify()
		self.assertEqual(s.listify(), [99,1,2,10])

		x = SinglyLinkedList()
		self.assertEqual(x.listify(), [])

	def testContains(self):
		s = SinglyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)
		self.assertTrue(s.contains(3))
		self.assertFalse(s.contains(5))

	def testDelete(self):
		s = SinglyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)
		s.deleteNodeValue(4)
		self.assertEqual(s.listify(), [1,2,3])

		s.deleteNodeValue(1)
		self.assertEqual(s.listify(), [2,3])

		s.deleteNodeValue(3)
		self.assertEqual(s.listify(), [2])

if __name__ == '__main__':
    unittest.main()

