# node class
class Node:

	def __init__(self, value, linked_node=None):
		self.value = value
		self.linked_node = linked_node

	# returns value of node	
	def get_value(self):
		return self.value

	# returns linked node	
	def get_linked_node(self):
		return self.linked_node

	# sets value
	def set_value(self, value):
		self.value = value	

	# sets linked node
	def set_linked_node(self, linked_node):
		self.linked_node = linked_node
