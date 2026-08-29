from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def path_finder(root: Node, target):
    result = _path_finder(root, target)
    if result is None:
        return None
    else:
        return result[::-1]

def _path_finder(root: Node, target):
    if root is None:
        return None
    if root.val == target:
        return [ root.val ]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None
    

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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

    res = path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]
    print(res)