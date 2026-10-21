class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def pre_order_traversal(self, root: BinaryTreeNode):
        self._pre_order_traversal(root)
        print()

    def _pre_order_traversal(self, root: BinaryTreeNode):
        if root is None:
            return
        print(root.val, end=" ")
        self._pre_order_traversal(root.left)
        self._pre_order_traversal(root.right)

    def in_order_traversal(self, root: BinaryTreeNode):
        self._in_order_traversal(root)
        print()

    def _in_order_traversal(self, root: BinaryTreeNode):
        if root is None:
            return
        self._in_order_traversal(root.left)
        print(root.val, end= " ")
        self._in_order_traversal(root.right)