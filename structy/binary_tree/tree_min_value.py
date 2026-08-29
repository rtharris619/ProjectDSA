from structy.helpers.binary_tree_helper import BinaryTreeNode as Node
from math import inf

def tree_min_value(root: Node):
    min_value = inf
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val < min_value:
            min_value = current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return min_value

def tree_min_value_rec(root: Node):
    if root is None:
        return inf
    min_left = tree_min_value_rec(root.left)
    min_right = tree_min_value_rec(root.right)
    return min(root.val, min_left, min_right)

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
    res = tree_min_value_rec(a) # -> -2
    print(res)