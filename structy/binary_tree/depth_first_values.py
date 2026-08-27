from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def depth_first_values(root: Node):
    if root is None:
        return []
    stack = [ root ]
    values = []
    while stack:
        current = stack.pop()
        values.append(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return values

def depth_first_values_rec(root: Node):
    if root is None:
        return []
    left_values = depth_first_values_rec(root.left)
    right_values = depth_first_values_rec(root.right)
    return [root.val] + left_values + right_values

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')        
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    res = depth_first_values_rec(a) # -> ['a', 'b', 'd', 'e', 'c', 'f']
    print(res)