from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def post_order(root):
    values = []
    traverse(root, values)
    return values

def traverse(root, values):
    if root is None:
        return
    traverse(root.left, values)
    traverse(root.right, values)
    values.append(root.val)

def driver():
    x = Node('x')
    y = Node('y')
    z = Node('z')

    x.left = y
    x.right = z

    #       x
    #    /    \
    #   y      z

    res = post_order(x) # ['y', 'z', 'x']
    print(res)

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
    c.left = f
    c.right = g
    
    #      a
    #    /    \
    #   b      c
    #  / \    / \
    # d   e  f   g

    res = post_order(a) # [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
    print(res)