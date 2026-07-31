import algomonster.helpers.binary_tree_helper as bt

def find_maximum(root: bt.Node):
    if root is None:
        return float('-inf')
    return max(root.val, find_maximum(root.left), find_maximum(root.right))

def find_maximum_local(root: bt.Node, current_max: int):
    if root is None:
        return current_max

    left_max = find_maximum_local(root.left, current_max)
    right_max = find_maximum_local(root.right, current_max)

    return max(root.val, left_max, right_max)

max_val = float('-inf')

def find_maximum_global(root: bt.Node):
    global max_val
    if root is None:
        return
    if root.val > max_val:
        max_val = root.val
    find_maximum_global(root.left)
    find_maximum_global(root.right)

def driver():
    encoded_tree = "5 9 2 x x 3 x x 8 7 x x 11 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)

    result = find_maximum(root)
    print(result)

    result = find_maximum_local(root, float('-inf'))
    print(result)

    find_maximum_global(root)
    print(max_val)