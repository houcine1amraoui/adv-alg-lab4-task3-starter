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
        """
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

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
        """
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
            # 1. Perform a normal BST insertion
            #    - If the current root is empty:
            #          → create a new node and return it
            #
            #    - Otherwise:
            #          → if value is smaller, insert into LEFT subtree
            #          → if value is larger, insert into RIGHT subtree
            #
            #    - After inserting, update root.left or root.right accordingly
            # -------------------------------

            # -------------------------------
            # 2. Update the height of the current root
            #    height = 1 + max(height(left subtree), height(right subtree))
            # -------------------------------

            # -------------------------------
            # 3. Compute the balance factor of this node
            #    balance = height(left subtree) - height(right subtree)
            # -------------------------------

            # -------------------------------
            # 4. Check the 4 imbalance cases and apply rotations
            #
            #   Case 1: Left-Left imbalance
            #       - balance > 1
            #       - value was inserted in LEFT subtree of LEFT child
            #       → perform RIGHT rotation on root
            #
            #   Case 2: Right-Right imbalance
            #       - balance < -1
            #       - value was inserted in RIGHT subtree of RIGHT child
            #       → perform LEFT rotation on root
            #
            #   Case 3: Left-Right imbalance
            #       - balance > 1
            #       - value inserted in RIGHT subtree of LEFT child
            #       → rotate LEFT on left child, then RIGHT on root
            #
            #   Case 4: Right-Left imbalance
            #       - balance < -1
            #       - value inserted in LEFT subtree of RIGHT child
            #       → rotate RIGHT on right child, then LEFT on root
            # -------------------------------

            # -------------------------------
            # 5. Return the (possibly rotated) root node
            # -------------------------------
            pass
        self.root = _insert(self.root, value)

