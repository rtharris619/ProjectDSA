from typing import Optional

class TreeNode:
  def __init__(self, val = 0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root:
    return None
  
  temp = root.left
  root.left = root.right
  root.right = temp

  invert_tree(root.right)
  invert_tree(root.left)

  return root


def traversal(root: TreeNode) -> TreeNode:
  if not root:
    return None
  
  print(root.val, end=',')
  traversal(root.left)
  traversal(root.right)


def tests():
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(7)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(9)
  traversal(root)
  print()
  res = invert_tree(root)
  traversal(res)


def driver():
  tests()
