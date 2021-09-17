class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    # adds child node to self.children
    def add_child(self, child_node):
        self.children.append(child_node)

    # removes child node from self.children
    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

    # traverse tree and print out values of all nodes
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children    