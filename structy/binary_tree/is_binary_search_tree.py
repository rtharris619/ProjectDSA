# Write a function, is_binary_search_tree, that takes in the root of a binary tree. 
# The function should return a boolean indicating whether or not the tree satisfies the binary search tree property.
# A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value 
# and all values in a node's right subtree are greater than the node's value.

from structy.helpers.binary_tree_helper import BinaryTree, BinaryTreeNode as Node

def is_binary_search_tree(root):
    values = []
    traverse(root, values)
    for i in range(0, len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def traverse(root, values):
    if root is None:
        return
    traverse(root.left, values)
    values.append(root.val)
    traverse(root.right, values)

def driver():
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   9     19

    res = is_binary_search_tree(a) # -> True
    print(res)

    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(15)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   15     19

    res = is_binary_search_tree(a) # -> False
    print(res)