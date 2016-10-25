class Node(object):
	
	# Initializes node with value of None
	def __init__(self, value = None):
		self.value = value
		self.next = None
		self.prev = None
	
	# Override object to string to be the node value
	def __str__(self):
		return str(self.value)
	