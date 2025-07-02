
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def good_nodes(root: TreeNode) -> int:
  
  def dfs(node: TreeNode, maxValue: int):
    if not node:
      return 0
    
    result = 1 if node.val >= maxValue else 0
    maxValue = max(maxValue, node.val)
    result += dfs(node.left, maxValue)
    result += dfs(node.right, maxValue)

    return result
  
  return dfs(root, root.val)


def preorder_traversal(root: TreeNode):
  if not root:
    return
  print(root.val, end=', ')
  preorder_traversal(root.left)
  preorder_traversal(root.right)
    

def test1():
  root = TreeNode(3)
  root.left = TreeNode(1)
  root.left.left = TreeNode(3)
  root.right = TreeNode(4)
  root.right.left = TreeNode(1)
  root.right.right = TreeNode(5)
  res = good_nodes(root)
  print(res)
  preorder_traversal(root)


def tests():
  test1()


def driver():
  tests()
