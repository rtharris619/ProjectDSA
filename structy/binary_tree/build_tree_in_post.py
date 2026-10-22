# Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. 
# The function should build a binary tree that has the given in-order and post-order traversal structure. 
# The function should return the root of this tree.

# You can assume that the values of inorder and postorder are unique.

from structy.helpers.binary_tree_helper import BinaryTree, BinaryTreeNode as Node

def build_tree_in_post(in_order, post_order):
    if len(in_order) == 0:
        return None

    # retrieve root node from last element of post order.
    val = post_order[-1]
    root = Node(val)

    # split the in-order array down the middle from the matching root node value.
    mid = in_order.index(val)
    left_in_order = in_order[0:mid]
    right_in_order = in_order[mid+1:]

    # this part is a bit weird...
    left_post_order = post_order[:len(left_in_order)]
    right_post_order = post_order[len(left_in_order):-1]

    root.left = build_tree_in_post(left_in_order, left_post_order)
    root.right = build_tree_in_post(right_in_order, right_post_order)

    return root

def driver():
    res = build_tree_in_post(
        [ 'y', 'x', 'z' ],
        [ 'y', 'z', 'x' ] 
    )
    #      x
    #    /   \
    #   y     z
    BinaryTree().pre_order_traversal(res)

    res = build_tree_in_post(
        [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
        [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
    )
    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h
    BinaryTree().pre_order_traversal(res)
