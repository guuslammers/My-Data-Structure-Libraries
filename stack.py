from node import Node

class Stack:

	def __init__(self, size_limit=1000):
		self.top_item = None
		self.size_limit = size_limit
		self.size = 0

	# peek at the top item on the stack	
	def peek(self):
		if not self.is_empty():
			return self.top_item.get_value()
		else:
			print('stack is empty')	

	# push item onto top of stack	
	def push(self, value):
		if self.has_space():
			new_item = Node(value)
			new_item.set_linked_node(self.top_item)
			self.top_item = new_item
			self.size += 1
		else:
			print('stack is full')	

	# pops and returns item on top of stack
	def pop(self):
		if not self.is_empty():
			item_to_remove = self.top_item
			self.top_item = item_to_remove.get_linked_node()
			self.size -= 1
			return item_to_remove.get_value()
		else:
			print('stack is empty')	

	# checks if stack is full		
	def has_space(self):
		if self.size_limit > self.size:
			return True
		else:
			return False	

	# checks if stack is empty		
	def is_empty(self):		 		
		if self.size == 0:
			return True
		else:
			return False	

