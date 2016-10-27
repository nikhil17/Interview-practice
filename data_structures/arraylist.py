import unittest

# This class uses lists to make an arraylist
# Assumes lists are of fixed size like java arrays

class ArrayList(object):
	def __init__(self):
		self.DEFAULT_CAPACITY = self.size = 10
		self.filled_values = 0
		self.my_list = list()
		#initializing array to None

		for i in range(self.DEFAULT_CAPACITY):
			# print i
			self.my_list.append(None)
		print self.my_list

	def __str__(self):
		return str(self.my_list)

	def add(self, value):
		# double the size of the backing array
		if self.filled_values == self.size:
			newSize = self.size *2
			new_list = list()
			#init empty list
			for i in range(newSize):
				new_list.append(None)
			
			for i in range(self.size):
				new_list.insert(i, self.my_list.index(i))
			self.my_list = new_list
			self.size = newSize
		
		self.my_list.insert(self.filled_values,value)
		self.filled_values += 1

		

x = ArrayList()
x.add(9)
print x