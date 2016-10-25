from node import Node2
from SinglyLinkedList import MyList
import unittest

class DoublyLinkedList(MyList):
	def __init__(self):
		super(DoublyLinkedList, self).__init__()
	
	#adds at the end of the list
	def add(self, value):
		n = Node2(value)
		if self.head == None:
			self.head = self.tail = n

		else:
			self.tail.next = n
			n.prev, self.tail = self.tail, n

			
		self.size += 1

	def addToHead(self, value):
		n = Node2(value)
		if self.head == None:
			self.head = self.tail = n
		else:
			n.next, self.head.prev = self.head, n
			self.head = n
		self.size += 1

	def iterateBackward(self):
		curr = self.tail
		while (curr):
			yield curr
			curr = curr.prev

	def deleteNode(self, value):
		found = False
		curr, p = self.head, None

		if self.head.value == value:
			found = True
			if self.size is 1:
				self.head = self.tail = None
			else:
				n = self.head.next
				n.prev, self.head = None, n
		elif (self.tail.value == value):
			found = True
			p = self.tail.prev
			p.next, self.tail = None, p

		else:
			while curr and not found:
				if curr.value is value:
					found = True
					n = curr.next
					p.next, n.prev = n, p
				curr, p = curr.next, curr

		if found:
			self.size -= 1
		else:
			print str(value) + ' is not in the list'
				
	
	

class UnitTestDoublyLinkedList(unittest.TestCase):
	def testAdd(self):
		s = DoublyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)

		self.assertEqual(s.listify(), [1,2,3])
		
		

	def testContains(self):
		s = DoublyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)
		self.assertTrue(s.contains(3))
		self.assertFalse(s.contains(5))

	def testDelete(self):
		s = DoublyLinkedList()
		s.add(1)
		s.add(2)
		s.add(3)
		
		s.deleteNode(2)
		self.assertEqual(s.listify(), [1,3])
		s.deleteNode(2)

		s.deleteNode(1)
		self.assertEqual(s.listify(), [3])

if __name__ == '__main__':
    unittest.main()

