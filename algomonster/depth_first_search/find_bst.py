import algomonster.helpers.binary_tree_helper as bt

def find_bst(bst: bt.Node, target: int) -> bool:
    if bst is None:
        return False
    if bst.val == target:
        return True
    if bst.val > target:
        return find_bst(bst.left, target)
    else:
        return find_bst(bst.right, target)

def driver():
    encoded_tree = "8 5 2 x 3 x x 6 x x 10 x 14 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    res = find_bst(root, 7)
    print(res)
