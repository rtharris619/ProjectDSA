from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:

  res = []

  def traverse(node: TreeNode):
    if not node:
      return
    
    traverse(node.left)

    if len(res) == k:
      return [res]
    else:
      res.append(node.val)
    
    traverse(node.right)

  traverse(root)

  return res[-1]


def test1():
  root = TreeNode(3)
  root.left = TreeNode(1)
  root.left.right = TreeNode(2)
  root.right = TreeNode(4)
  res = kth_smallest(root, 1)
  print(res)


def tests():
  test1()


def driver():
  tests()
