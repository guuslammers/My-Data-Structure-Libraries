from Node import Node

class Linked_List:
	
	def __init__(self, value=None):
		self.head = Node(value)

	# get head node	
	def get_head(self):
		return self.head	

	# inserts node at beggining
	def insert_beggining(self, value=None):
		# instantiate new node
		new_node = Node(value)
		# link new node to current head node
		new_node.set_linked_node(self.head)
		# set new node to be new head node
		self.head = new_node

	# inserts node at end
	def insert_end(self, value=None):
		# instantiate new node
		new_node = Node(value)
		current_node = self.get_head()
		# iterate to end of list and add new node
		while current_node:
			# get next node
			next_node = current_node.get_linked_node()
			# if next node is None the end of the list has been reached
			if next_node == None:
				# insert new node
				current_node.set_linked_node(new_node)
				# break loop
				current_node = None
			else:
				current_node = next_node	


	# print list
	def print_list(self):
		list_string = ''
		current_node = self.get_head()
		# loop through linked list
		while current_node:
			# if value is not None
			if current_node.get_value() != None:
				list_string += str(current_node.get_value()) + '\n'
			# get next node	
			current_node = current_node.get_linked_node()	
		# print list	
		print(list_string)	

	# get length of list
	def get_length(self):
		count = 0
		current_node = self.head
		# iterate through list
		while current_node:	
			count += 1
			current_node = current_node.get_linked_node()
		return count		

	# remove node with value		
	def remove_node_value(self, value):
		current_node = self.get_head()
		# if current nodes value is equal to value
		if current_node.get_value() == value:
			# set head to be next node
			self.head = current_node.get_linked_node()
		else:
			# while current node is not None
			while current_node:
				# get next node
				next_node = current_node.get_linked_node()
				# if next node value is equal to value
				if next_node.get_value() == value:
					# link current node to next next node
					current_node.set_linked_node(next_node.get_linked_node())
					# break loop
					current_node = None
				else:
					current_node = next_node	

	# remove node at index		
	def remove_node_index(self, index):
		current_node = self.head
		# if index is 0
		if index == 0:
			# set head to next node
			self.head = current_node.get_linked_node()
		else:	
			# iterate to node at index - 1
			for i in range(index - 1):
				current_node = current_node.get_linked_node()
			# link current node to next next node
			current_node.set_linked_node(current_node.get_linked_node().get_linked_node())

			
l = Linked_List('Guus')			
l.print_list()
l.insert_beggining('Kylee')
l.print_list()
l.insert_end('Lexy')
l.print_list()
print(l.get_length())
l.remove_node_value('Lexy')
l.print_list()
l.remove_node_index(0)
l.print_list()