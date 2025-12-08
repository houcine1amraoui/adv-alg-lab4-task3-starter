class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Define a helper recursive function that takes a node and a value
        # 1. If the current node is None:
        #    → We reached an empty spot in the tree
        #    → Create a new node with the given value and return it
        # 2. If the value is less than the current node's value:
        #    → Recursively insert into the LEFT subtree
        #    → Update node.left with the result of the recursive call
        # 3. Otherwise (value is greater or equal):
        #    → Recursively insert into the RIGHT subtree
        #    → Update node.right with the result
        # 4. Return the current node (to maintain tree structure)

        # Start insertion from the root
        # Update the root since the recursive function returns a subtree
        pass