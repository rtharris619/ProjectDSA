import algomonster.helpers.binary_tree_helper as bt

def post_order_traversal(root: bt.Node) -> None:
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)

def driver():
    helper = bt.BinaryTreeHelper()
    encoded_tree = "5 4 3 x x 8 x x 6 x x"
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    post_order_traversal(root)