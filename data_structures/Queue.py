from singly_linked_list import MyList
from node import Node
import unittest


class Queue(MyList):
    def __init__(self):
        super(Queue, self).__init__()
    
    #appends to tail O(1)
    def enqueue(self, value):
        if not value:
            print 'Attempted to pass invalid value'
            return
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    # pops off head O(1)
    def dequeue(self):
        if not self.head:
            print 'Queue is empty empty empty'
            return

        if self.head == self.tail:
            x = self.head
            self.tail = self.head = None
            return

        n = self.head
        self.head = self.head.next
        return n

    def peek(self):
        if not self.head:
            print 'Queue is empty'
        else: return self.head

class UnitTestQueue(unittest.TestCase):
    def test1(self):
        q = Queue()
        q.enqueue(None)

        self.assertEqual(q.listify(), [])
        q.enqueue(2)
        q.dequeue()
        q.dequeue()


        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.listify(), [3,4])




if __name__ == '__main__':
    unittest.main()
