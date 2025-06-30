
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
  
  current = root
  while current:
    if current.val > p.val and current.val > q.val:
      current = current.left
    elif current.val < p.val and current.val < q.val:
      current = current.right
    else:
      return current
  

def test1():
  T = TreeNode(6)
  T.left = TreeNode(2)
  T.right = TreeNode(8)
  T.left.left = TreeNode(0)
  T.left.right = TreeNode(4)
  T.left.right.left = TreeNode(3)
  T.left.right.right = TreeNode(5)
  T.right.left = TreeNode(7)
  T.right.right = TreeNode(9)

  res = lowest_common_ancestor(T, T.left, T.right)
  print(res.val)


def tests():
  test1()


def driver():
  tests()
