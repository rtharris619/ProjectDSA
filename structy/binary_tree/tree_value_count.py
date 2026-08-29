from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def tree_value_count_rec(root: Node, target: int):
    if root is None:
        return 0
    match = 1 if root.val == target else 0
    return match + tree_value_count_rec(root.left, target) + tree_value_count_rec(root.right, target)

def tree_value_count(root: Node, target: int):
    if root is None:
        return 0
    count = 0
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            count += 1
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return count

def driver():
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4   6     12

    res = tree_value_count_rec(a,  6) # -> 3
    print(res)