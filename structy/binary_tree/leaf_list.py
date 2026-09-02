from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def leaf_list_rec(root: Node):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    left_side = leaf_list_rec(root.left)
    right_side = leaf_list_rec(root.right)
    return [*left_side, *right_side]

def leaf_list(root: Node):
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            res.append(current.val)        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res

def driver():
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    res = leaf_list(a) # -> [ 20, 1, 3, 54 ]
    print(res)
