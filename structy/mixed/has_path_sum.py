# Write a function, has_path_sum, that takes in the root of a binary tree and a target number.
# The function should return a boolean indicating whether or not there is a path through the tree that sums to the target.

# A path must begin at the root and end at a leaf.


from structy.helpers.binary_tree_helper import BinaryTreeNode as Node


def has_path_sum(root, target):
    if root is None:
        return False
    # ending a path at a leaf
    if root.left is None and root.right is None and target == root.val:
        return True
    
    new_target = target - root.val
    return has_path_sum(root.left, new_target) or has_path_sum(root.right, new_target)


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

    res = has_path_sum(a, 8) # -> True
    print(res)