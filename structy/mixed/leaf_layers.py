# Write a function, leaf_layers, that takes in the root of a binary tree.
# The function should return a 2D list where each sublist represents a "leaf layer" of the tree.

# To get a leaf layer, take all leaf nodes in tree. Then, conceptually "remove" them from the tree.
# This will create new "leaves". Repeat this process until the tree is empty.

# You don't need to actually delete the nodes from the tree, just return the list of layers.

from structy.helpers.binary_tree_helper import BinaryTreeNode as Node


def leaf_layers(root):
    layers = []
    get_height(root, layers)
    return layers

def get_height(root: Node, layers: list[list[str]]):
    if root is None:
        return -1
    left_side = get_height(root.left, layers)
    right_side = get_height(root.right, layers)
    height = 1 + max(left_side, right_side)

    if len(layers) == height:
        layers.append([])
    layers[height].append(root.val)

    return height

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

    res = leaf_layers(a) # ->
    # [
    #   ['d', 'e', 'f'],
    #   ['b', 'c'],
    #   ['a']
    # ]
    print(res)

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")
    i = Node("i")

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
    #     g  h   i

    # leaf_layers(a) # ->
    # [
    #   ['d', 'g', 'h', 'i'],
    #   ['e', 'f'],
    #   ['b', 'c'],
    #   ['a'],
    # ]
