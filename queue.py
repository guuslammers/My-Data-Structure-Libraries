from node import Node

class Queue:

	def __init__(self, max_size=None):
		self.head = None
		self.tail = None
		self.max_size = max_size
		self.size = 0

	# returns item at front of queue	
	def peek(self):
		if self.get_size() > 0:
			return self.head.get_value()
		else:
			print('Queue is empty.')	

	# returns size of queue	
	def get_size(self):
		return self.size	

	# returns true if queue has space	
	def has_space(self):
		if not self.max_size:
			return True
		elif self.max_size > self.size:
			return True
		else:
			return False

	# return true if queue is empty		
	def is_empty(self):
		if self.size == 0:
			return True
		else:
			return False

	# add item to back of queue		
	def enqueue(self, value):
		if self.has_space():
			item_to_add = Node(value)

			if self.is_empty():
				self.head = item_to_add
				self.tail = item_to_add

			else:
				self.tail.set_linked_node(item_to_add)
				self.tail = item_to_add

			self.size += 1					

		else:
			print('Queue is full.')

	# remove and return the head of queue
	def dequeue(self):
		if not self.is_empty():
			item_to_remove = self.head

			if self.size == 1:
				self.head = None
				self.tail = None

			else:
				self.head = item_to_remove.get_linked_node()

			self.size -= 1
			
			return item_to_remove.get_value()

		else:
			print('Queue is empty.')					
