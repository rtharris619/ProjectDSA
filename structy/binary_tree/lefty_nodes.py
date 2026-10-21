# Write a function, lefty_nodes, that takes in the root of a binary tree.
# The function should return a list containing the left-most value on every level of the tree.
# The list must be ordered in a top-down fashion where the root is the first item.
# Note that the left-most node on a level may not necessarily be a left child.

from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def lefty_nodes(root):
    values = []
    _lefty_nodes(root, 0, values)
    return values

def _lefty_nodes(root, level, values):
    if root is None:
        return
    if len(values) == level:
        values.append(root.val)
    level += 1
    _lefty_nodes(root.left, level, values) # Important to travel left before travelling right!
    _lefty_nodes(root.right, level, values)

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
    #   g   h

    res = lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]
    print(res)

    u = Node('u')
    t = Node('t')
    s = Node('s')
    r = Node('r')
    q = Node('q')
    p = Node('p')

    u.left = t
    u.right = s
    s.right = r
    r.left = q
    r.right = p

    #     u
    #  /    \
    # t      s
    #         \
    #         r
    #        / \
    #        q  p

    res = lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]
    print(res)