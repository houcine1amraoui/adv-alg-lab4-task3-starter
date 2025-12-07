class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # height of node in AVL tree

class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None: return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # -------------------------
    # Rotations
    # -------------------------
    def rotate_right(self, z):
        """
        Right rotation:
                z                              y
              /   \                          /   \
             y     T4   ---->               x     z
           /   \                          /  \   / \
          x     T3                       T1  T2 T3 T4
         / \                          
        T1 T2                    
        """
        # Store references
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z # y becomes new root
        z.left = T3 # z becomes right child of y, T3 becomes left child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root after rotation

    def rotate_left(self, z):
        """
        Left rotation:
            z                                   y
          /   \                               /   \
         T1    y       ----->                z     x
              /  \                          / \   / \
             T2   x                        T1 T2 T3 T4
                 / \
                T3 T4                        
        """
        # Store references
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root after rotation

    # AVL Insert (Recursive)
    def insert(self, value):
        def _insert(node, value):
            # 1. Normal BST insertion

            # 2. Update height of this node
            

            # 3. Compute balance factor
            

            # 4. Rotation cases

            # Case 1: Left Left
            if balance > 1 and value < node.left.value:
                return self.rotate_right(node)

            # Case 2: Right Right
            if balance < -1 and value > node.right.value:
                return self.rotate_left(node)

            # Case 3: Left Right
            if balance > 1 and value > node.left.value:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            # Case 4: Right Left
            if balance < -1 and value < node.right.value:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node  # return (possibly updated) subtree root

        self.root = _insert(self.root, value)
