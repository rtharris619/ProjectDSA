# Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values.
# The function should return the value of the lowest common ancestor of the two values in the tree.
# You may assume that the tree values are unique and the tree is non-empty.
# Note that a node may be considered an ancestor of itself.

from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

# 1. Find paths to both targets
# 2. Find first common value among paths

def path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [target]
    left_path = path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    right_path = path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path
    return None

def lowest_common_ancestor(root, val1, val2):
    path_1 = path_finder(root, val1)
    path_2 = set(path_finder(root, val2))
    for item in path_1:
        if item in path_2:
            return item

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

    res = lowest_common_ancestor(a, 'd', 'h') # b
    print(res)
