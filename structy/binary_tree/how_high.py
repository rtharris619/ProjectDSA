from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def how_high_rec(root: Node):
    if root is None:
        return -1
    left_side = how_high_rec(root.left)
    right_side = how_high_rec(root.right)
    return 1 + max(left_side, right_side)

def how_high(root: Node):
    if root is None:
        return -1
    stack = [(root, 0)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        if node.left:
            stack.append((node.left, height + 1))
        if node.right:
            stack.append((node.right, height + 1))
    return max_height

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    res = how_high(a) # -> 3
    print(res)