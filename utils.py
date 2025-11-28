def height(node):
    if node is None: return 0
    left_h = height(node.left)
    right_h = height(node.right)
    return 1 + max(left_h, right_h)

def balance_factor(node):
    if node is None: return 0
    return height(node.left) - height(node.right)