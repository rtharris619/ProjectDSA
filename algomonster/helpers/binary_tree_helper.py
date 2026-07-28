class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeHelper:
    def build_tree(self, nodes, f):
        val = next(nodes)
        if val == 'x':
            return None
        left = self.build_tree(nodes, f)
        right = self.build_tree(nodes, f)
        return Node(f(val), left, right)