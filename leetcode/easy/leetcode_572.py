from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  
def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

  if not subRoot: return True
  if not root: return False

  def same_tree(p, q):
    if not p and not q:
      return True
    if p and q and p.val == q.val:
      return (same_tree(p.left, q.left) and 
              same_tree(p.right, q.right))

    return False
  
  if same_tree(root, subRoot):
    return True
  
  return (is_subtree(root.left, subRoot) or 
          is_subtree(root.right, subRoot))


def test1():
  root = TreeNode(3)
  root.right = TreeNode(5)
  root.left = TreeNode(4)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(2)

  subroot = TreeNode(4)
  subroot.left = TreeNode(1)
  subroot.right = TreeNode(2)

  print(is_subtree(root, subroot))


def test2():
  root = TreeNode(3)
  root.right = TreeNode(5)
  root.left = TreeNode(4)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(2)
  root.left.right.left = TreeNode(0)

  subroot = TreeNode(4)
  subroot.left = TreeNode(1)
  subroot.right = TreeNode(2)

  print(is_subtree(root, subroot))


def tests():
  test1()
  test2()


def driver():
  tests()
