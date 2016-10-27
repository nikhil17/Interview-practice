from singly_linked_list import MyList
from node import Node
import unittest

class Stack(MyList):
    def __init__(self):
        super(Stack, self).__init__()
    
    # Pushes to head of list in O(1)
    def push(self, value):
        if not value:
            print 'Attempted to push bad value'
            return
        n = Node(value)
        n.next = self.head
        self.head = n

    def peek(self):
        if not self.head:
            print 'Stack is empty'
            return
        return self.head

    def pop(self):
        if not self.head:
            print 'Attempted to pop off empty stack'
            return None
        n1, n2 = self.head, self.head.next
        self.head = n2
        return n1

class UnitTestStack(unittest.TestCase):
    def test_1(self):
        s = Stack()
        s.push(2)
        s.push(3)
        s.push(34)
        s.push(5)
        s.push(6)


        self.assertEqual(s.listify(), [6, 5, 34, 3, 2])
        s.pop()
        self.assertEqual(s.listify(), [5, 34, 3, 2])
        
        s.push(None)
        self.assertEqual(s.peek().value, 5)
        self.assertEqual(s.listify(), [5, 34, 3, 2])

        s.pop()
        s.pop()
        s.pop()
        s.pop()

        self.assertEqual(s.listify(), [])


        s.push(None)
        self.assertEqual(s.listify(), [])


if __name__ == '__main__':
    unittest.main()


