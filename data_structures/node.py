class Node(object):
	
	# Initializes node with value of None
	def __init__(self, value = None):
		self.value = value
		self.next = None
	
	# Override object to string to be the node value
	def __str__(self):
		return str(self.value)

#Node with previous pointer for doubly linked list
class Node2(Node):
	def __init__(self, value = None):
		self.prev = None
		super(Node2, self).__init__(value)       