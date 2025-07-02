from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
  diameter = [0]

  def dfs(node: TreeNode):
    if not node:
      # height of null tree is -1 to help us with the math
      return -1 
    left = dfs(node.left)
    right = dfs(node.right)
    # Diameter (constant of 2 because we can go left and right)
    diameter[0] = max(diameter[0], 2 + left + right)
    # Height
    return 1 + max(left, right)
  
  dfs(root)

  return diameter[0]


def inorder_traversal(root: TreeNode):
  if not root:
    return
  
  inorder_traversal(root.left)
  print(root.val, end=', ')
  inorder_traversal(root.right)


def tests():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print(diameter_of_binary_tree(root))


def driver():
  tests()
