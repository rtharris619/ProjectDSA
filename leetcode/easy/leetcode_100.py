from typing import Optional
from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

  def dfs(p, q):
    if not p and not q:
      return True
    if (not p or not q) or (p.val != q.val):
      return False
    
    return dfs(p.left, q.left) and dfs(p.right, q.right)
    
  return dfs(p, q)


def is_same_tree_2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  
  stack = [[p, q]]
  while stack:
    pnode, qnode = stack.pop()
    if pnode and qnode:
      if pnode.val != qnode.val:
        return False
      else:
        stack.append([pnode.left, qnode.left])
        stack.append([pnode.right, qnode.right])
    elif (pnode and not qnode) or (not pnode and qnode):
      return False
  
  return True


def test1():
  p = TreeNode(1)
  p.left = TreeNode(2)
  p.right = TreeNode(3)

  q = TreeNode(1)
  q.left = TreeNode(2)
  q.right = TreeNode(3)

  print(is_same_tree_2(p, q))


def test2():
  p = TreeNode(1)
  p.left = TreeNode(2)

  q = TreeNode(1)
  q.right = TreeNode(2)

  print(is_same_tree_2(p, q))


def test3():
  p = TreeNode(1)
  p.left = TreeNode(2)
  p.right = TreeNode(1)

  q = TreeNode(1)
  q.left = TreeNode(1)
  q.right = TreeNode(2)

  print(is_same_tree_2(p, q))


def tests():
  test1()
  test2()
  test3()


def driver():
  tests()
