# Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree.
# The function should build a binary tree that has the given in-order and pre-order traversal structure.
# The function should return the root of this tree.

# You can assume that the values of inorder and preorder are unique.

from structy.helpers.binary_tree_helper import BinaryTree, BinaryTreeNode as Node

def build_tree_in_pre(in_order, pre_order):
    if len(in_order) == 0:
        return None
    val = pre_order[0]
    root = Node(val)

    mid = in_order.index(val)
    left_in_order = in_order[:mid]
    right_in_order = in_order[mid + 1:]
    left_pre_order = pre_order[1:len(left_in_order) + 1]
    right_pre_order = pre_order[len(left_in_order) + 1:]

    root.left = build_tree_in_pre(left_in_order, left_pre_order)
    root.right = build_tree_in_pre(right_in_order, right_pre_order)

    return root

def build_tree_in_pre_2(in_order, pre_order):
    in_order_index = {}
    for i in range(len(in_order)):
        ele = in_order[i]
        in_order_index[ele] = i
    return _build_tree_in_pre(in_order, pre_order, (0, len(in_order) - 1), (0, len(in_order) - 1), in_order_index)

def _build_tree_in_pre(in_order, pre_order, in_order_indices, pre_order_indices, in_order_index):
        
    in_order_start, in_order_end = in_order_indices
    pre_order_start, pre_order_end = pre_order_indices

    if in_order_end < in_order_start:
        return None

    val = pre_order[pre_order_start]
    root = Node(val)

    mid = in_order_index[val]
    left_size = mid - in_order_start

    left_in_order_range =   (in_order_start, mid - 1)
    left_pre_order_range =  (pre_order_start + 1, pre_order_start + left_size)

    right_in_order_range =  (mid + 1, in_order_end)
    right_pre_order_range = (pre_order_start + left_size + 1, pre_order_end)

    root.left = _build_tree_in_pre(in_order, pre_order, left_in_order_range, left_pre_order_range, in_order_index)
    root.right = _build_tree_in_pre(in_order, pre_order, right_in_order_range, right_pre_order_range, in_order_index)

    return root

def driver():
    res = build_tree_in_pre_2(
        [ 'z', 'y', 'x' ],
        [ 'y', 'z', 'x' ] 
    )
    #       y
    #    /    \
    #   z      x
    BinaryTree().post_order_traversal(res)

    res = build_tree_in_pre_2(
        [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
        [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
    )
    #       a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h
    BinaryTree().post_order_traversal(res)