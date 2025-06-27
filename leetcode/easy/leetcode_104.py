from typing import Optional
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    
  def dfs(node: TreeNode):
    if not node:
      return 0
    
    left = dfs(node.left)
    right = dfs(node.right)

    return 1 + max(left, right)
  
  return dfs(root)


# BFS Iterative
def max_depth_2(root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  
  lvl = 0
  q = deque([root])
  while q:
    for _ in range(len(q)):
      node = q.popleft()
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    
    lvl += 1

  return lvl


# DFS Iterative
def max_depth_3(root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  
  lvl = 1
  stack = [[root, 1]]
  while stack:
    node, depth = stack.pop()
    if node:
      lvl = max(lvl, depth)
      stack.append([node.left, depth + 1])
      stack.append([node.right, depth + 1])

  return lvl


def traverse_tree(root: Optional[TreeNode]):
  if not root:
    return
  
  print(root.val, end=', ')
  traverse_tree(root.left)
  traverse_tree(root.right)


def tests():
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  traverse_tree(root)
  print()
  print('Max:', max_depth_3(root))


def driver():
  tests()
