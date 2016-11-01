import unittest

class MinHeap(object):
    def __init__(self):
        self._list = [0]
        self._size = 0

    def insert(self, value):
        if value:
            self._list.append(value)
            self._size += 1
            self.swapUp()

    def swapUp(self):
        i = self._size
        while (self._list[i] < self._list[i/2] and i > 1):
            temp = self._list[i]
            self._list[i], self._list[i/2] = self._list[i/2], temp

    def printList(self):
        print 'printing list'
        x = [i for i in range(self._size+ 1)]
        print x
        print self._list
        print

    def peek(self):
        if self._size >= 1:
            return self._list[1]
        else:
            print "Heap is empty"
            return None

    def pop(self):
        if self._size < 1:
            print 'Heap is empty'
            return

        if self._size == 1:
            self._size -= 1
            return self._list.pop()

        val = self._list[1]
        self._list[1] = self._list[self._size]
        self._list.pop()
        self._size -= 1
        self.swapDown()
        print 'popped '+ str(val)


    def swapDown(self):
        i = 1
        mIndex = self.getMinChildIndex(i)
        while i < self._size and mIndex:
            self._list[i], self._list[mIndex] =  self._list[mIndex], self._list[i]
            i = mIndex
            mIndex = self.getMinChildIndex(i)

    def getMinChildIndex(self, cur): 
        #gets the index of the child of the node of index cur
        # with the lower value, defaulting to the left child if equal
        if cur > self._size:
            print 'overflow bad'
            return None

        if (cur * 2 + 1) <= self._size:
            #both children are valid
            if (self._list[cur*2 + 1] < self._list[cur] or self._list[cur*2] < self._list[cur]):
                return (cur * 2) if self._list[cur*2] <= self._list[cur*2 + 1] else cur*2 + 1
            #return None if node at index cur is > than both left and right children
            else: return None

        if cur * 2 == self._size and self._list[cur*2] < self._list[cur]:
            #only left child is valid
            return cur * 2
        #returns None if cur has no children
        return None



class testHeap(unittest.TestCase):
    def test(self):
        x = MinHeap()
        x.insert(19)
        x.printList()
        x.insert(10)
        x.insert(5)
        x.insert(16)
        x.insert(None)
        x.printList()
        self.assertEqual(x._list, [0, 5, 16, 10, 19])
        x.pop()
        self.assertEqual(x._list, [0, 10, 16, 19])
        x.pop()
        self.assertEqual(x._list, [0, 16, 19])
        x.pop()
        x.pop()
        self.assertEqual(x._list, [0])
        x.insert(5)
        x.insert(19)
        x.insert(10)
        x.insert(16)
        x.insert(8)




        
        x.printList()

if __name__ == '__main__':
    unittest.main()


