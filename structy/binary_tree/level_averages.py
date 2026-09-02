from structy.helpers.binary_tree_helper import BinaryTreeNode as Node

def level_averages(root: Node):
    if root is None:
        return []
    levels = []
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        if len(levels) <= level:
            levels.append([])
        levels[level].append(node.val)
        if node.left:
            stack.append((node.left, level + 1))
        if node.right:
            stack.append((node.right, level + 1))
    res = []
    for level in levels:
        avg = sum(level) / len(level)
        res.append(avg)
    return res

def _fill_levels(root: Node, levels: list[list], level: int):
    if root is None:
        return []
    if len(levels) <= level:
        levels.append([])
    levels[level].append(root.val)

    _fill_levels(root.left, levels, level + 1)
    _fill_levels(root.right, levels, level + 1)
 
def level_averages_rec(root: Node):
    levels = []
    _fill_levels(root, levels, 0)
    res = []
    for level in levels:
        avg = sum(level) / len(level)
        res.append(avg)
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

    res = level_averages_rec(a) # -> [ 5, 32.5, 17.5, 2 ] 
    print(res)