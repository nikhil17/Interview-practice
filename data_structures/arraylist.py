import unittest

# This class uses lists to make an arraylist
# Assumes lists are of fixed size like java arrays

class ArrayList(object):
    def __init__(self):
        self.DEFAULT_CAPACITY = self.size = 10
        self._filled_values = 0
        self._my_list = list()
        #initializing array to None

        for i in range(self.DEFAULT_CAPACITY):
            # print i
            self._my_list.append(None)

    def get_list(self):
        return self._my_list

    def __str__(self):
        return str(self._my_list)

    def add(self, value):
        # double the size of the backing array
        if value == None:
            print 'Unable to add None to arraylist'
            return
        if self._filled_values == self.size:
            newSize = self.size *2
            new_list = list()
            #init empty list
            for i in range(newSize):
                new_list.append(None)
            
            for i in range(self.size):
                new_list[i] = self._my_list[i]
            self._my_list = new_list
            self.size = newSize
        
        self._my_list[self._filled_values] = value
        self._filled_values += 1

    def get(self, index):
        if index < self._filled_values and index >= 0:
            return self._my_list[index]
        else:
            print 'Invalid index'

    def remove(self, index):
        # print (index < self._filled_values & index >= 0)
        if index < self._filled_values and index >= 0:
            self._filled_values -= 1
            self.size -= 1
            return self._my_list.pop(index)

        else: 
            print 'Attempted to remove invalid index'

class array_list_test(unittest.TestCase):
    def test(self):
        x = ArrayList()
        x.add(9)
        x.add(10)
        x.add(10)
        x.add(11)
        x.add(10)
        self.assertEqual(x.get_list(), [9, 10, 10, 11, 10, None, None, None, None, None])
        x.remove(1)
        self.assertEqual(x.get_list(), [9, 10, 11, 10, None, None, None, None, None])
        x.remove(0)
        x.remove(0)
        x.remove(0)
        x.remove(0)
        self.assertEqual(x.get_list(), [None, None, None, None, None])
        self.assertEqual(x.size, 5)
        self.assertEqual(x._filled_values, 0)

        x.remove(0)
        self.assertEqual(x.size, 5)
        self.assertEqual(x._filled_values, 0)

        x.add(10)
        x.add(11)
        x.add(12)
        x.add(13)
        x.add(14)
        self.assertEqual(x.get_list(), [10,11,12,13,14])
        
        x.add(5)
        self.assertEqual(x.get_list(), [10,11,12,13,14,5,None, None, None, None])

if __name__ == '__main__':
    unittest.main()