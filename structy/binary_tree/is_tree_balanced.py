# Write a function, is_tree_balanced, that takes in the root of a binary tree.
# The function should return a boolean indicating whether or not the tree is "balanced".

# A "balanced" binary tree is a binary tree where the height between the left and right subtrees differs by at most 1 for every node.

from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def is_tree_balanced(root):
    return True if _is_tree_balanced(root) >= 0 else False

def _is_tree_balanced(root):
    if root is None:
        return 0
    left_height = _is_tree_balanced(root.left)
    if left_height == -1:
        return -1
    right_height = _is_tree_balanced(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")

    a.left = b
    a.right = c

    #         a
    #       /   \
    #      b    c

    res = is_tree_balanced(a) # -> True
    print(res)

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.left = b
    a.right = c
    b.right = d

    #         a
    #       /   \
    #      b    c
    #      \
    #      d

    res = is_tree_balanced(a) # -> True
    print(res)

    a = Node("a")
    b = Node("b")
    c = Node("c")

    a.right = b
    b.right = c

    #        a
    #         \
    #          b
    #          \
    #           c

    res = is_tree_balanced(a) # -> False
    print(res)