from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def tree_sum_rec(root: Node):
    if root is None:
        return 0
    return root.val + tree_sum_rec(root.left) + tree_sum_rec(root.right)

from collections import deque
def tree_sum_queue(root: Node):
    if root is None:
        return 0
    total = 0
    queue = deque([root])
    while queue:
        current = queue.pop()
        total += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return total

def tree_sum_stack(root: Node):
    if root is None:
        return 0
    total = 0
    stack = [root]
    while stack:
        current = stack.pop()
        total += current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return total

def driver():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    res = tree_sum_stack(a) # -> 21
    print(res)