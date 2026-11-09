# Write a function, flatten_tree, that takes in the root of a binary tree.
# The function should modify the binary tree by flattening it into a "linked-list" using the same tree nodes.
# In the resulting "linked-list", left pointers should be null and right pointers should point to the next node in the list.
# The order of the nodes in the resulting "linked-list" should follow pre-order.
# Your function should return the root/head of the list.

# You can assume the tree contains at least one node.

# For example, this tree:
#         a
#       /   \
#     b      c
#    / \      \
#   d   e      f

# Should be flattened into:
#       a
#        \
#         b
#          \
#           d
#            \
#             e
#              \
#               c
#                \
#                 f


from structy.helpers.binary_tree_helper import BinaryTree, BinaryTreeNode as Node


def flatten_tree(root: Node):
    stack = [ root ]
    prev: Node = None

    while stack:
        current = stack.pop()
        if prev:
            prev.right = current
        prev = current

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        current.left = None
        current.right = None

    return root


def traverse(root: Node):
    _traverse(root)
    print()


def _traverse(root: Node):
    if root is None:
        return
    print(root.val, end=" ")
    _traverse(root.right)


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

    res = flatten_tree(a) # ->
    #      a
    #       \
    #        b
    #         \
    #          d
    #           \
    #            e
    #            \
    #             c
    #              \
    #               f
    traverse(res)