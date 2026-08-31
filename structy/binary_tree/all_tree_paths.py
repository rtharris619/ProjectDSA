from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def all_tree_paths(root: Node):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()
    return paths

def _all_tree_paths(root: Node):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []
    left_paths = _all_tree_paths(root.left)
    for path in left_paths:
        path.append(root.val)
        all_paths.append(path)

    right_paths = _all_tree_paths(root.right)
    for path in right_paths:
        path.append(root.val)
        all_paths.append(path)

    return all_paths

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /   
    #     g   h  i 

    res = all_tree_paths(a) # ->
    # [ 
    #   [ 'a', 'b', 'd' ], 
    #   [ 'a', 'b', 'e', 'g' ], 
    #   [ 'a', 'b', 'e', 'h' ], 
    #   [ 'a', 'c', 'f', 'i' ] 
    # ] 
    print(res)