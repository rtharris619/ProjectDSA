from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
  
  def dfs(node: TreeNode, left: int, right: int):
    if not node:
      return True
    
    if not (node.val > left and node.val < right):
      return False
    
    return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

  return dfs(root, float('-inf'), float('inf'))


def test1():
  root = TreeNode(2)
  root.left = TreeNode(1)
  root.right = TreeNode(3)
  print(is_valid_bst(root))


def test2():
  root = TreeNode(5)
  root.left = TreeNode(1)
  root.right = TreeNode(4)
  print(is_valid_bst(root))


def test3():
  root = TreeNode(2)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  print(is_valid_bst(root))

def tests():
  test1()
  test2()
  test3()


def driver():
  tests()
