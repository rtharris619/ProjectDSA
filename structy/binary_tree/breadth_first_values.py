from structy.helpers.binary_tree_helper import BinaryTreeNode as Node
from collections import deque

def breadth_first_values(root: Node):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values

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

    res = breadth_first_values(a) # -> ['a', 'b', 'c', 'd', 'e', 'f']
    print(res)