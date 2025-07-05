from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  
def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
  if not preorder or not inorder:
    return None
  
  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])
  # Recurse every node to the left of mid
  root.left = build_tree(preorder[1:mid+1], inorder[:mid])
  # Recurse every node to the right of mid
  root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

  return root


def traverse(root: TreeNode):
  if not root:
    return
    
  traverse(root.left)
  print(root.val, end=',')
  traverse(root.right)


def test1():
  preorder = [3,9,20,15,7]
  inorder =  [9,3,15,20,7]
  build_tree(preorder, inorder)


def tests():
  test1()


def driver():
  tests()
