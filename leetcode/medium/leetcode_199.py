from typing import List, Optional
from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
  res = []
  if not root:
    return res
  
  queue = deque([root])
  while queue:
    lastnode = TreeNode()
    for _ in range(len(queue)):
      lastnode = queue.popleft()
      if lastnode.left:
        queue.append(lastnode.left)
      if lastnode.right:
        queue.append(lastnode.right)
    res.append(lastnode.val)
  
  return res


def test1():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.left.right = TreeNode(5)
  root.right = TreeNode(3)
  root.right.right = TreeNode(4)
  print(right_side_view(root))


def test2():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.left.left = TreeNode(4)
  root.left.left.left = TreeNode(5)
  root.right = TreeNode(3)
  print(right_side_view(root))


def tests():
  test1()
  test2()

def driver():
  tests()
