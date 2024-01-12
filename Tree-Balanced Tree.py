class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True

    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

def get_height(node):
    if node is None:
        return 0

    left_height = get_height(node.left)
    right_height = get_height(node.right)

    return max(left_height, right_height) + 1
