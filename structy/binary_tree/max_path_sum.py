from structy.helpers.binary_tree_helper import BinaryTreeNode as Node
from math import inf

def max_path_sum_rec(root: Node):
    if root is None:
        return -inf
    if root.left is None and root.right is None: # I've reached a leaf node
        return root.val
    left_max = max_path_sum_rec(root.left)
    right_max = max_path_sum_rec(root.right)
    return root.val + max(left_max, right_max)

def driver():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    res = max_path_sum_rec(a) # -> 18
    print(res)