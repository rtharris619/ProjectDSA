import algomonster.helpers.binary_tree_helper as bt

def find_target(root: bt.Node, target: int) -> bt.Node:
    if root is None:
        return
    if root.val == target:
        return root
    
    left = find_target(root.left, target)
    right = find_target(root.right, target)

    return left or right

def find_target_2(root: bt.Node, target: int) -> bt.Node:
    if root is None:
        return
    if root.val == target:
        return root
    return find_target_2(root.left, target) or find_target_2(root.right, target)

def driver():
    encoded_tree = "1 2 3 x 5 x x 4 x x 6 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    target = 4

    res = find_target_2(root, target)
    if res:
        print(res.val)
    else:
        print("not found")