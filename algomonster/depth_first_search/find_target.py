import algomonster.helpers.binary_tree_helper as bt

def dfs(root: bt.Node, target: int) -> bt.Node:
    if root is None:
        return
    if root.val == target:
        return root
    
    left = dfs(root.left, target)
    right = dfs(root.right, target)

    return left or right

def driver():
    encoded_tree = "1 2 3 x 5 x x 4 x x 6 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    target = 7

    res = dfs(root, target)
    if res:
        print(res.val)
    else:
        print("not found")