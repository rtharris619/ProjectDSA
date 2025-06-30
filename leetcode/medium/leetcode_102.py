from typing import Optional, List
from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:

  if not root:
    return []

  res = [[]]
  q = deque([root])

  while q:
    sub_res = []
    for _ in range(len(q)):
      node = q.popleft()
      sub_res.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    res.append(sub_res)

  return res[1:]


def tests():
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  print(level_order(root))


def driver():
  tests()
