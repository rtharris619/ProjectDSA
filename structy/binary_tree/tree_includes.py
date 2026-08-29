from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def tree_includes_rec(root: Node, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return tree_includes_rec(root.left, target) or tree_includes_rec(root.right, target)

from collections import deque
def tree_includes(root: Node, target) -> bool:
    if root is None:
        return False
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

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

    res = tree_includes(a, "e") # -> True
    print(res)