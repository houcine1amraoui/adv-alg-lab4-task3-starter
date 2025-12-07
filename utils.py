def height(node):
    if node is None: return 0
    left_h = height(node.left)
    right_h = height(node.right)
    return 1 + max(left_h, right_h)

def balance_factor(node):
    if node is None: return 0
    return height(node.left) - height(node.right)

def print_bst(root, level=0, prefix="Root: "):
    if root is not None:
        print("    " * level + prefix + str(root.value))
        print_bst(root.left, level + 1, "L--- ")
        print_bst(root.right, level + 1, "R--- ")
