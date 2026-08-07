import algomonster.helpers.binary_tree_helper as bt

def invert_binary_tree(tree: bt.Node) -> bt.Node:
    if tree is None:
        return None
    return bt.Node(
        tree.val, 
        invert_binary_tree(tree.right), 
        invert_binary_tree(tree.left))


def driver():
    encoded_tree = "1 2 4 x 7 x x 5 x x 3 x 6 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    res = invert_binary_tree(root)
    print(res.val)