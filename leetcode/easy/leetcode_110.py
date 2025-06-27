from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# height differences must be one or zero to be balanced
def is_balanced(root: Optional[TreeNode]):

  def dfs(node: Optional[TreeNode]):
    if not node:
      return [True, 0]
    
    left = dfs(node.left)
    right = dfs(node.right)

    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

    return [balanced, 1 + max(left[1], right[1])]
  
  return dfs(root)[0]


def is_balanced_2(root: Optional[TreeNode]) -> bool:
  if not root:
    return True

  stack = [[root, 1]]
  level = 1

  while stack:
    node, depth = stack.pop()
    if node:
      print(level, depth)
      level = max(level, depth)
      
      left = node.left
      right = node.right
      stack.append([left, depth + 1])
      stack.append([right, depth + 1])

  return False


def test1():
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  # print(is_balanced(root))
  is_balanced_2(root)


def test2():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(3)
  root.left.left.left = TreeNode(4)
  root.left.left.right = TreeNode(4)
  # print(is_balanced(root))
  is_balanced_2(root)


def tests():
  # test1()
  test2()


def driver():
  tests()
