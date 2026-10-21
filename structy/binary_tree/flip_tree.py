# Write a function, flip_tree, that takes in the root of a binary tree.
# The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa.
# This flipping should occur in-place by modifying the original tree.
# The function should return the root of the tree.

from structy.helpers.binary_tree_helper import BinaryTree, BinaryTreeNode as Node

def flip_tree(root):
    if root is None:
        return
    
    left_side = flip_tree(root.left) # gives me back the root of the left subtree
    right_side = flip_tree(root.right) # gives me back the root of the right subtree
    root.left = right_side
    root.right = left_side
    
    return root

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    / \
    #   g   h

    res = flip_tree(a)
    BinaryTree().pre_order_traversal(res)

    #       a
    #    /    \
    #   c      b
    #  /     /   \
    # f     e    d
    #     /  \
    #    h    g
