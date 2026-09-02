from structy.helpers.binary_tree_helper import BinaryTreeNode as Node
from collections import deque

def tree_levels(root: Node):
    if root is None:
        return []
    res = []
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        if len(res) <= level:
            res.append([])
        res[level].append(node.val)
        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))

    return res

def tree_levels_2(root: Node):
    if root is None:
        return []
    res = []
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        if len(res) <= level:
            res.append([])
        res[level].append(node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return res

def tree_levels_rec(root: Node):
    levels = []
    _fill_levels(root, levels, 0)
    return levels

def _fill_levels(root: Node, levels, level: int):
    if root is None:
        return []
    
    if len(levels) <= level:
        levels.append([])
    levels[level].append(root.val)

    _fill_levels(root.left, levels, level + 1)
    _fill_levels(root.right, levels, level + 1)

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

    res = tree_levels_rec(a) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f'],
    #   ['g', 'h', 'i']
    # ]
    print(res)