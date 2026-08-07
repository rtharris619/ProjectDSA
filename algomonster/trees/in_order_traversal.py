import algomonster.helpers.binary_tree_helper as bt

def in_order_traversal(root: bt.Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

def driver():
    helper = bt.BinaryTreeHelper()
    encoded_tree = "5 4 3 x x 8 x x 6 x x"
    bst = helper.build_tree(iter(encoded_tree.split(" ")), int)
    in_order_traversal(bst)
